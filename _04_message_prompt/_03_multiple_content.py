# -*- coding: utf-8 -*-
# @Time    : 2026/10/6
# @Author  : Ari
# @File    : _03_multiple_content.py
# @Desc    : multiple content

from langchain.chat_models import init_chat_model
import base64

from langchain_core.messages import HumanMessage

model = init_chat_model(model_name="gpt-4", model_provider="openai", temperature=0.5, api_key="YOUR_API_KEY")


def encode_image(img_path):
    """将一张本地图片转换成 Base64 编码的 Data URI 字符串,方便在文本中嵌入图片数据"""
    with open(img_path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode("utf-8")

# 获取图像base64编码字符串
img_path = "input/image_test.png"
base64_image = encode_image(img_path)

msg = model.invoke(
    [
        HumanMessage(
            content_blocks=[
                {"type": "text", "content": "请分析以下图片内容，并给出详细描述："},
                {"type": "image", "content": base64_image, "format": "base64", "alt_text": "分析图片"}
            ]
        )
    ]
)
print(msg.content)
