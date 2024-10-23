from docx import Document 
import json
import PyPDF2
from PyPDF2 import PdfReader

from PyPDF2 import PdfReader


pdf_file = open(r"C:\Users\admin\OneDrive\Desktop\sedra.pdf", "rb")


pdf_reader = PdfReader(pdf_file)


num_pages = len(pdf_reader.pages)


for page in range(num_pages):
    page_obj = pdf_reader.pages[page]
    print(page_obj.extract_text())


pdf_file.close()



