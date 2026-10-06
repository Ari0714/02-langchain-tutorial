# -*- coding: utf-8 -*-
# @Time    : 2026/10/6
# @Author  : Ari
# @File    : _04_prompt_template.pyf
# @Desc    : partial / placeholder usage

from langchain.chat_models import init_chat_model
from langchain_core.prompts import PromptTemplate, ChatPromptTemplate

model = init_chat_model(model_provider="")

prompt_template = ChatPromptTemplate([
    ("system", "你是一个有帮助的AI机器人，你的department是{name}。"),
    ("human", "你好，最近怎么样？"),
    ("ai", "我很好，谢谢！"),
    ("human", "{user_input}")
])

### partial
sale_department = prompt_template.partial(name="Sales")
tech_department = prompt_template.partial(name="Tech")

sale_value = sale_department.invoke({"user_input": "how much burn last project?"})
tech_value = tech_department.invoke({"user_input": "how to solve this issue?"})

model.invoke(sale_value)
model.invoke(tech_value)

### placeholder
prompt_template2 = ChatPromptTemplate.from_messages([
    ("system", "你是一个有用的AI助手"),
    ("placeholder", "{conversation}"),
])
placeholder_value = prompt_template2.invoke({
    "conversation": [
        ("human", "你好!"),
        ("ai", "今天我能帮你做什么？"),
        ("human", "你能给我做一个冰激凌吗？"),
        ("ai", "抱歉，我没有这样的能力")
    ]
})
