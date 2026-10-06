# -*- coding: utf-8 -*-
# @Time    : 2026/10/6
# @Author  : Ari
# @File    : _03_invoke_openrouter.py
# @Desc    : invoke openrouter api, which is a middle-router platform for LLMs, including DeepSeek, OpenAI, etc.

import os


from langchain_openrouter import ChatOpenRouter
from dotenv import load_dotenv

load_dotenv(override=True)
api_key = os.getenv("DEEPSEEK_API_KEY")
base_url = os.getenv("DEEPSEEK_BASE_URL")

chartbot = ChatOpenRouter(
    api_key=api_key,
    # base_url=base_url,
    model="deepseek/deepseek-v4-flash"
)

print(chartbot.invoke("what Guangzhou tomorrow weather?"))

#### use ChatopenAi also fine, need populate openrouter base_url in .env file

#### use closeai also fine, need populate closeai base_url in .env file
from langchain_openai import ChatOpenAI
base_url_closeai = os.getenv("CLOSEAI_BASE_URL")
chartbot = ChatOpenAI(
    api_key=api_key,
    base_url=base_url_closeai,
    model="deepseek/deepseek-v4-flash"
)