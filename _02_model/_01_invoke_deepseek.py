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

print(chartbot.invoke("what Guangzhou tomorrow weather?"))


## same as Zhipu / Qianwen
from langchain_community.chat_models import ChatQianWen
from langchain_community.chat_models import ChatZhipu

## most of them compatible ChatOpenAi
from langchain_openai import ChatOpenAI