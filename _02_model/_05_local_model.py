# -*- coding: utf-8 -*-
# @Time    : 2026/10/6
# @Author  : Ari
# @File    : _05_local_model.py
# @Desc    : local model usage: Ollama. illusion issue explicit

from langchain_ollama import ChatOllama
from langchain.chat_models import init_chat_model

model = ChatOllama(model="deepseek-r1:1.5b", base_url="http://localhost:11434")
chartMsg = model.invoke("Write a poem about the beauty of nature.")
print(chartMsg.content)

# use init_chat_model
model2 = init_chat_model(model="deepseek-r1:1.5b", model_provider="ollama", baseusr="http://localhost:11434")
