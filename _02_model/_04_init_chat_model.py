# -*- coding: utf-8 -*-
# @Time    : 2026/10/6
# @Author  : Ari
# @File    : _04_init_chat_model.py
# @Desc    : usage init_chat_model

from langchain.chat_models import init_chat_model
from dotenv import load_dotenv
import os

load_dotenv(override=True)
api_key = os.getenv("DEEPSEEK_API_KEY")
base_url = os.getenv("DEEPSEEK_BASE_URL")

model = init_chat_model(
    model_provider="openai", # use ChatOpenAI as foundation
    model="deepseek-v4-flash",
    base_url=base_url,
    temperature=0.5,   # higher temperature means more randomness, lower means more deterministic
    max_tokens=1024,
    api_key=api_key)

chatMsg = model.invoke("Hello, how are you?")

print(chatMsg.content)
