# -*- coding: utf-8 -*-
# @Time    : 2026/10/6
# @Author  : Ari
# @File    : _01_longsmith_test.py
# @Desc    : longsmith test


from langchain.chat_models import init_chat_model

# trace model info autoly through .env file
model = init_chat_model(model_provider="openai", model_name="gpt-3.5-turbo", temperature=0.7, api_key="YOUR_API_KEY")
msg = model.invoke("Hello, how are you?")
print(msg.content)

