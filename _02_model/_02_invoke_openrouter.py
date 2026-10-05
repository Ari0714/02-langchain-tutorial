import os
from langchain_openrouter import ChatOpenRouter
from dotenv import load_dotenv

load_dotenv(override=True)
# api_key = os.getenv("DEEPSEEK_API_KEY")
# base_url = os.getenv("DEEPSEEK_BASE_URL")

chartbot = ChatOpenRouter(
    # api_key=api_key,
    # base_url=base_url,
    model="deepseek-v4-flash"
)

print(chartbot.invoke("what Guangzhou tomorrow weather?"))


