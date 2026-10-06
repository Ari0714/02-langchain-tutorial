# -*- coding: utf-8 -*-
# @Time    : 2026/10/6
# @Author  : Ari
# @File    : _02_universal_usage.py
# @Desc    : ChatOpenAI model usage example, compatible with DeepSeek API....


from langchain_openai import ChatOpenAI
import os
from dotenv import load_dotenv

load_dotenv()
base_url = os.getenv("DEEPSEEK_BASE_URL")
api_key = os.getenv("DEEPSEEK_API_KEY")

client = ChatOpenAI(
    model="deepseek-v4-flash",
    base_url = base_url,
    api_key = api_key
)

chat_msg = client.invoke("Hello, world!")

print(chat_msg.content)