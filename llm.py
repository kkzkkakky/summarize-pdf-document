import openai
import os
from langchain.chat_models import ChatOpenAI

os.environ['OPENAI_API_KEY'] = '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'
openai.api_key = os.getenv('OPENAI_API_KEY')

llm = ChatOpenAI(temperature=0, model_name='gpt-3.5-turbo')

