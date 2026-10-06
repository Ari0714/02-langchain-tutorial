# -*- coding: utf-8 -*-
# @Time    : 2026/10/6
# @Author  : Ari
# @File    : _04_prompt_template.py
# @Desc    : prompt template: 1. ChatPromptTemplate support message while PromptTemplate not

from langchain.chat_models import init_chat_model
from langchain_core.prompts import PromptTemplate, ChatPromptTemplate
from langchain_core.output_parsers import OutputParser

# temp = PromptTemplate.from_template("use one sentence explain {topic}, i am a {identity}")
prompt_template = ChatPromptTemplate.from_template("use one sentence explain {topic}, i am a {identity}")
# prompt_value = prompt_template.invoke({"topic": "cartoon", "identity": "elementary student"})
# prompt_value = prompt_template.format(topic="cartoon", identity="elementary student")

model = init_chat_model(model_provider="")

parse = OutputParser()

chain = prompt_template | model | parse

res = chain.invoke({
    "topic": "cartoon", "identity": "elementary student"
})
print(res.content)


### ChatPromptTemplate message
msg_prompt_template = ChatPromptTemplate.from_messages([
    ("system", "你是一个有帮助的AI机器人，你的名字是{name}。"),
    ("human", "你好，最近怎么样？"),
    ("ai", "我很好，谢谢！"),
    ("human", "{user_input}")
])
template_value = msg_prompt_template.invoke({"name":"小明", "user_input":"你叫什么名字？"})
res = model.invoke(template_value)
print(res.content)
