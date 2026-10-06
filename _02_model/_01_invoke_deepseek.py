# -*- coding: utf-8 -*-
# @Time    : 2026/10/6
# @Author  : Ari
# @File    : _01_langchain_test.py
# @Desc    : invoke deepseek api

import os
from langchain_deepseek import ChatDeepSeek
from dotenv import load_dotenv

load_dotenv(override=True)
# api_key = os.getenv("DEEPSEEK_API_KEY")
# base_url = os.getenv("DEEPSEEK_BASE_URL")

chartbot = ChatDeepSeek(
    # api_key=api_key,
    # base_url=base_url,
    model="deepseek-v4-flash"
)

chat_content = chartbot.invoke("what Guangzhou tomorrow weather?")
print(chat_content.content.encode("utf-8").decode())


## same as Zhipu / Qianwen
from langchain_community.chat_models import ChatTongyi
from langchain_community.chat_models import ChatZhipuAI

