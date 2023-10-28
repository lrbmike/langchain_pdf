from fastapi import APIRouter, Body, Request
import openai

router = APIRouter(
    prefix="/ai"
)


@router.post("/chat")
async def chat(
        request: Request,
        text: str = Body(embed=True)
):
    # 使用session缓存对话
    messages = request["session"].get("messages")
    if messages is None:
        messages = [{"role": "system", "content": "你是一个全职妈妈，了解很多小朋友喜欢的故事，知识面很广"}]

    user_chat = {"role": "user", "content": text}
    messages.append(user_chat)

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages
    )

    content = response.choices[0].message.content

    # 添加ai的回复
    ai_chat = {"role": "assistant", "content": content}
    messages.append(ai_chat)

    # 处理messages的长度，避免token过长
    messages = messages[0: 10]

    # 重新保存到session
    request["session"]["messages"] = messages

    return response


@router.post("/image")
async def image(
        text: str = Body(embed=True)
):
    response = openai.Image.create(prompt=text)

    return response


@router.post("/clean_session")
async def clean_session(
        request: Request
):
    request.session.clear()
    return {'success': True}
