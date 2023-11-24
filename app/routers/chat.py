from fastapi import APIRouter, Body, Request

from app.tool.llm import LlmEngine
from app.tool.store import FaissEngine

router = APIRouter(
    prefix="/chat"
)


@router.post("/question")
async def question(
        text: str = Body(embed=True)
):
    faiss = FaissEngine()
    vector_store = faiss.load_vector_store()

    llm = LlmEngine()
    chain = llm.get_qa_chain(vector_store)

    response = chain({"query": text})
    # reply = "回复:"
    return {'success': True, "code": 0, "reply": response}


@router.post("/question_history")
async def question_history(
        request: Request,
        text: str = Body(embed=True)
):
    faiss = FaissEngine()
    vector_store = faiss.load_vector_store()

    llm = LlmEngine()
    chain = llm.get_history_chain(vector_store)

    # 使用session缓存对话
    chat_history = request["session"].get("chat_history")
    if chat_history is None:
        chat_history = []

    # Convert chat history to list of tuples
    chat_history_tuples = []
    for message in chat_history:
        chat_history_tuples.append((message[0], message[1]))

    response = chain({"question": text, "chat_history": chat_history_tuples})

    # 保存聊天记录
    chat_history.append((text, response["answer"]))
    # 处理chat_history的长度，避免token过长
    chat_history = chat_history[0: 10]

    # 重新保存到session
    request["session"]["chat_history"] = chat_history

    # reply = "回复:"
    return {'success': True, "code": 0, "reply": response}
