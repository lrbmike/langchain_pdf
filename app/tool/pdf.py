from PyPDF2 import PdfReader


class PdfEngine:

    def __init__(self, pdf):
        self.pdf = pdf

    # 获取pdf文件内容
    def get_pdf_text(self):
        text = ""
        pdf_reader = PdfReader(self.pdf)
        for page in pdf_reader.pages:
            text += page.extract_text()

        return text
