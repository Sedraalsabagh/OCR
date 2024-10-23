from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
from io import StringIO


pdf_path = r"C:\Users\admin\OneDrive\Desktop\sedra.pdf"

def pdf_to_text(pdf_path):
    manager = PDFResourceManager()
    output = StringIO()
    converter = TextConverter(manager, output, laparams=LAParams())
    interpreter = PDFPageInterpreter(manager, converter)

    with open(pdf_path, 'rb') as file:
        for page in PDFPage.get_pages(file, check_extractable=True):
            interpreter.process_page(page)

        text = output.getvalue()

    converter.close()
    output.close()

    return text


text = pdf_to_text(pdf_path)
print(text)
