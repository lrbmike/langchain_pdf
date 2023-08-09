from PyPDF2 import PdfReader


# 获取pdf文件内容
def get_pdf_text(pdf):
    text = ""
    pdf_reader = PdfReader(pdf)
    for page in pdf_reader.pages:
        text += page.extract_text()

    return text
