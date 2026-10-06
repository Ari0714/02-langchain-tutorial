# -*- coding: utf-8 -*-
# @Time    : 2026/10/6
# @Author  : Ari
# @File    : _07_stream_async_batch.py
# @Desc    : stream / async / batch invoke


from langchain.chat_models import init_chat_model
import asyncio

# stream
model = init_chat_model(model_provider="openai", model_name="gpt-3.5-turbo", temperature=0.7, api_key="YOUR_API_KEY")
chatMsg = model.stream("Hello, how are you?")
for chunk in chatMsg:
    print(chunk, end="", flush=True)

# batch
chatMsg3 = model.batch(
    ["Hello, how are you?",
     "What is the weather like today?"]
)
for i in chatMsg3:
    print(i)

# async
async def invoke_async():
    model = init_chat_model(model_provider="openai", model_name="gpt-3.5-turbo", temperature=0.7, api_key="YOUR_API_KEY")
    # await asyncio.create_task(model.ainvoke("Hello, how are you?"))
    chatMsg2 = await asyncio.gather(
        model.ainvoke("Hello, how are you?"),
        model.ainvoke("What is the weather like today?")
    )
    for msg in chatMsg2:
        print(msg)

if __name__ == '__main__':
    asyncio.run(invoke_async())