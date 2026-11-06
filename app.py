from pathlib import Path
from uuid import uuid4
from flask import Flask, render_template, request, send_from_directory, url_for
from werkzeug.utils import secure_filename
from src.main import extract_students, save_outputs

BASE_DIR = Path(__file__).resolve().parent
UPLOAD_DIR = BASE_DIR / "data" / "uploads"
OUTPUT_DIR = BASE_DIR / "data" / "output"
ALLOWED_EXTENSIONS = {"pdf"}
MAX_UPLOAD_BYTES = 15 * 1024 * 1024

UPLOAD_DIR.mkdir(parents=True, exist_ok=True)
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

app = Flask(__name__)
app.config["MAX_CONTENT_LENGTH"] = MAX_UPLOAD_BYTES


def allowed_file(filename):
    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route("/", methods=["GET", "POST"])
def index():
    error = None
    if request.method == "POST":
        uploaded = request.files.get("pdf_file")
        if not uploaded or not uploaded.filename:
            error = "Please choose a PDF file first."
        elif not allowed_file(uploaded.filename):
            error = "Only PDF files are supported."
        else:
            token = uuid4().hex[:10]
            safe_name = secure_filename(uploaded.filename) or "student_document.pdf"
            saved_pdf = UPLOAD_DIR / f"{token}_{safe_name}"
            uploaded.save(saved_pdf)
            try:
                extracted_text, students = extract_students(saved_pdf)
                excel_name = f"student_details_{token}.xlsx"
                text_name = f"extracted_text_{token}.txt"
                save_outputs(extracted_text, students, OUTPUT_DIR / excel_name, OUTPUT_DIR / text_name)
                return render_template(
                    "results.html",
                    students=students,
                    total=len(students),
                    source_name=safe_name,
                    excel_name=excel_name,
                    text_name=text_name,
                    extracted_text=extracted_text,
                )
            except Exception as exc:
                error = str(exc)
            finally:
                try:
                    saved_pdf.unlink(missing_ok=True)
                except OSError:
                    pass
    return render_template("index.html", error=error)


@app.route("/download/<path:filename>")
def download(filename):
    # Only generated files in the output directory can be downloaded.
    if Path(filename).name != filename or not filename.startswith(("student_details_", "extracted_text_")):
        return "File not found", 404
    return send_from_directory(OUTPUT_DIR, filename, as_attachment=True)


@app.errorhandler(413)
def file_too_large(_error):
    return render_template("index.html", error="The PDF is too large. Maximum upload size is 15 MB."), 413


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=False)
