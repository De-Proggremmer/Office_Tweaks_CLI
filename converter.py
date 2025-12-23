import docx2pdf, pdf2docx
import os
from decorators import log_errors

@log_errors
def convert_pdf_to_docx(file):
    i = 0
    while os.path.exists(file[:-3]+'docx'):
        i += 1
        file = file[:-4]+f"({i}).pdf"

    cv = pdf2docx.Converter(file)
    cv.convert()

@log_errors
def convert_docx_to_pdf(file):
    i = 0
    while os.path.exists(file[:-3] + 'pdf'):
        i += 1
        file = file[:-5] + f"({i}).docx"

    cv = docx2pdf.Converter(file)
    cv.convert()
