from fastapi import FastAPI, Request
# session中间件
from starlette.middleware.sessions import SessionMiddleware
from app.routers import chat
import sys
import os

from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())

# 防止相对路径导入出错
sys.path.append(os.path.join(os.path.dirname(__file__)))

app = FastAPI()
# 配置session，使用cookie方式保存
app.add_middleware(SessionMiddleware, secret_key='langchain_pdf_112233', max_age=86400, session_cookie='fast_api_sid')


@app.middleware("http")
async def some_middleware(request: Request, call_next):
    response = await call_next(request)
    session = request.cookies.get('session')
    if session:
        response.set_cookie(key='session', value=request.cookies.get('session'), httponly=True)
    return response


# 将其余单独模块进行整合
app.include_router(chat.router)
