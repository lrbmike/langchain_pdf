from fastapi import APIRouter, Body
from ..util import pdf, langchain, fass

router = APIRouter(
    prefix="/chat"
)

# 初始化pdf文件
@router.get("/init_pdf")
async def init_pdf():
    # pfd文件路径
    pdf_doc = ""

    # get pdf text
    raw_text = pdf.get_pdf_text(pdf_doc)

    # get the text chunks
    text_chunks = openai.get_text_chunks(raw_text)

    # save
    fass.save_vector_store(text_chunks)

    return {'success': True}


@router.post("/question")
async def question(
        text: str = Body(embed=True)
):
    vector_store = fass.load_vector_store()

    chain = langchain.get_qa_chain(vector_store)

    response = chain({"query": text})
    # reply = "回复:"
    return {'success': True, "code": 0, "reply": response}
