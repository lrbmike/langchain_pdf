from fastapi import FastAPI
from app.routers import chat
import sys
import os
from dotenv import load_dotenv, find_dotenv
import openai

load_dotenv(find_dotenv())
openai.api_key = os.getenv("OPENAI_API_KEY")
openai.api_base = os.getenv("OPENAI_API_BASE")

# 防止相对路径导入出错
sys.path.append(os.path.join(os.path.dirname(__file__)))

app = FastAPI()


# 将其余单独模块进行整合
app.include_router(chat.router)