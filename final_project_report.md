# FINAL PROJECT REPORT

## Project Title
Automated PDF Data Extraction

## 1. Introduction
This project focuses on extracting student information automatically from PDF documents using Python.

## 2. Objective
The main objective is to reduce manual data entry and save extracted information in Excel format.

## 3. Technologies Used
- Python
- PyMuPDF
- Pandas
- OpenPyXL
- Visual Studio Code

## 4. Project Workflow
1. Provide a PDF file as input.
2. Read PDF pages using PyMuPDF.
3. Extract text from the PDF.
4. Identify student details using Python regular expressions.
5. Organize the extracted information using Pandas.
6. Export the information into an Excel file.

## 5. Extracted Fields
- Student Name
- Roll Number
- Department
- Email Address

## 6. Error Handling
The application handles missing PDF files, invalid PDF files, and PDFs without matching student details.

## 7. Testing
The project was tested with valid, missing, and invalid PDF inputs. Automated checks were also created using Python unittest.

## 8. Output
The extracted student information is saved in:
`data/output/student_details.xlsx`

## 9. Limitations
The current version supports text-based PDFs. Scanned PDF documents requiring OCR are not yet supported.

## 10. Conclusion
The project demonstrates how Python can automate PDF text extraction and convert structured information into Excel format.

## 11. Future Enhancements
- Support multiple PDF files.
- Add OCR for scanned PDFs.
- Improve data validation.
- Generate detailed extraction reports.
