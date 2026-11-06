import pymupdf as fitz
import pandas as pd
import re
import os
pdf_path = "data/sample/sample_students.pdf"
output_path = "data/output/student_details.xlsx"
try:
    if not os.path.exists(pdf_path):
        raise FileNotFoundError("PDF file not found!")
    document = fitz.open(pdf_path)

    extracted_text = ""

    for page in document:
        extracted_text += page.get_text()

    document.close()

    students = []

    blocks = re.split(r"(?=Name:)", extracted_text)

    for block in blocks:
        name = re.search(r"Name:\s*(.*)", block)
        roll = re.search(r"Roll Number:\s*(.*)", block)
        department = re.search(r"Department:\s*(.*)", block)
        email = re.search(r"Email:\s*(.*)", block)

        if name and roll and department and email:
            students.append({
                "Name": name.group(1).strip(),
                "Roll Number": roll.group(1).strip(),
                "Department": department.group(1).strip(),
                "Email": email.group(1).strip()
            })

    if not students:
        raise ValueError("No student details found in PDF!")

    df = pd.DataFrame(students)
    df.to_excel(output_path, index=False)

    print("Data extracted successfully!")
    print("Excel saved:", output_path)

except Exception as error:
    print("Error:", error)