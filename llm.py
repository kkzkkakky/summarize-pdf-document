import openai
import os
from langchain.chat_models import ChatOpenAI

#ご自身のAPIキーを設定してください
os.environ["OPENAI_API_KEY"] = "***"
openai.api_key = os.getenv('OPENAI_API_KEY')

llm = ChatOpenAI(temperature=0, model_name='gpt-3.5-turbo')

