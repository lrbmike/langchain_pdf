import sys
import os
from dotenv import load_dotenv, find_dotenv

# 防止相对路径导入出错
sys.path.append(os.path.join(os.path.dirname(__file__)))

load_dotenv(find_dotenv('.env'))

from app.tool.pdf import PdfEngine
from app.tool.llm import LlmEngine
from app.tool.store import FaissEngine

# 将pdf切分块，嵌入和向量存储
if __name__ == '__main__':
    pdf_path = './test/demo.pdf'

    pfdEngine = PdfEngine(pdf_path)
    raw_text = pfdEngine.get_pdf_text()

    llmEngine = LlmEngine()
    text_chunks = llmEngine.get_text_chunks(raw_text)

    faissEngine = FaissEngine()
    faissEngine.save_vector_store(text_chunks)

    print(pdf_path + ' is ok')
