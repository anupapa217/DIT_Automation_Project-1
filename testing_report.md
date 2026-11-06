# Automated PDF Data Extraction

## 1. Project Overview
This project is developed to automatically extract student details from PDF documents and store the extracted information in an Excel file.

## 2. Project Objective
To reduce manual data entry by extracting information from PDF files using Python.

## 3. Technologies Used
- Python
- PyMuPDF
- Pandas
- OpenPyXL
- Visual Studio Code

## 4. Extracted Information
The system extracts:
- Student Name
- Roll Number
- Department
- Email Address

## 5. Project Folder Structure

```text
DIT_Automation_Project/
│
├── data/
│   ├── input/
│   ├── output/
│   └── sample/
│
├── src/
│   └── main.py
│
├── tests/
├── reports/
├── screenshots/
├── docs/
├── requirements.txt
└── README.md
```

## 6. Installation

Install the required Python packages:

```bash
py -m pip install -r requirements.txt
```

## 7. How to Run

1. Place the sample PDF inside `data/sample/`.
2. Open the project folder in VS Code.
3. Run the following command:

```bash
py src/main.py
```

4. Find the generated Excel file inside `data/output/`.

## 8. Output
The extracted student information is saved as:

`data/output/student_details.xlsx`

## 9. Error Handling
The program handles:
- Missing PDF files
- Invalid PDF files
- PDFs without matching student details

## 10. Testing
The project is tested using:
- Valid PDF files
- Missing PDF files
- Invalid PDF files

## 11. Current Limitation
The current prototype extracts text from text-based PDFs. Scanned PDFs requiring OCR are not yet supported.