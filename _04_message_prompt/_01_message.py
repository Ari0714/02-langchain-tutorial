# -*- coding: utf-8 -*-
# @Time    : 2026/10/6
# @Author  : Ari
# @File    : _01_message.py
# @Desc    : 4 types of message prompt: SystemMessage, HumanMessage, AIMessage, ToolMessage


from langchain.chat_models import init_chat_model
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage, ToolMessage

model = init_chat_model(model_provider="openai", model_name="gpt-3.5-turbo", temperature=0.7, api_key="YOUR_API_KEY")


message = [
    {"system": "You are a helpful assistant."},
    {"role": "user", "content": "Hello, how are you?"},
    {"role": "assistant", "content": "I'm doing well, thank you! How can I assist you today?"},
    {"role": "user", "content": "Can you tell me a joke?"}
]
model.invoke(message)


message2 = [
    SystemMessage(content="You are a helpful assistant."),
    HumanMessage(content="Hello, how are you?"),
    AIMessage(content="I'm doing well, thank you! How can I assist you today?"),
    HumanMessage(content="Can you tell me a joke?")
]
model.invoke(message2)
