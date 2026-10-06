# -*- coding: utf-8 -*-
# @Time    : 2026/10/6
# @Author  : Ari
# @File    : _02_toolmessage.py
# @Desc    : toolmessage example


from langchain.chat_models import init_chat_model
from langchain_core.messages import ToolMessage

model = init_chat_model(model_provider="openai", model_name="gpt-3.5-turbo", temperature=0.7, api_key="YOUR_API_KEY")

def get_weather(city):
    # Simulate fetching weather data for the given city
    return f"The current weather in {city} is sunny with a temperature of 25°C."

model.bind_tools([get_weather])

ai_msg = {
    "role": "assistant",
    "content": "I can provide weather information. Please provide a city name.",
    "tool_call": {
        "name": "get_weather",
        "id": "call_00_nUD2NC9QRN5Cg1GaoIkBJQ4s",
        "arguments": {
            "city": "New York"
        }
    }
}

tool_msg = {
    "role": "tool",
    "content": "The current weather in New York is sunny with a temperature of 25°C.",
    "tool_call_id": "call_00_nUD2NC9QRN5Cg1GaoIkBJQ4s"
}

msg = [
    {"role": "system", "content": "You are a helpful assistant."},
    ai_msg,
    tool_msg,
]

model.invoke(msg)
