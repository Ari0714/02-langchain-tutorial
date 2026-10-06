# -*- coding: utf-8 -*-
# @Time    : 2026/10/6
# @Author  : Ari
# @File    : _06_invoke.py
# @Desc    : usage of invoke

from langchain.chat_models import init_chat_model
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage

model = init_chat_model(model_provider="openai", model_name="gpt-3.5-turbo", temperature=0.7, api_key="YOUR_API_KEY")

# content
model.invoke("Hello, how are you?")

# dict
message = [
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": "Can you tell me a joke?"}
]
model.invoke(message)

# multiple dialogues
message2 = [
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": "Can you tell me a joke?"},
    {"role": "assistant", "content": "Why did the scarecrow win an award? Because he was outstanding in his field!"},
    {"role": "user", "content": "That's funny! Can you tell me another one?"}
]
model.invoke(message2)

# message class
message3 = [
    SystemMessage("Hello, how are you?"),
    HumanMessage("I'm doing well, thank you! How about you?"),
    AIMessage("I'm great, thanks for asking! What can I help you with today?"),
    HumanMessage("Can you tell me a story?")
]
model.invoke(message3)

# invoke return: AiMessage: id / content / response_metadata / usage_metadata

