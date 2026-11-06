
import unittest
import os

class TestPDFProject(unittest.TestCase):

    def test_sample_pdf_exists(self):
        self.assertTrue(
            os.path.exists("data/sample/sample_students.pdf")
        )

    def test_output_folder_exists(self):
        self.assertTrue(
            os.path.exists("data/output")
        )

    def test_requirements_file_exists(self):
        self.assertTrue(
            os.path.exists("requirements.txt")
        )

if __name__ == "__main__":
    unittest.main()
