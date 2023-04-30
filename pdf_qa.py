import openai
import platform
import openai
import chromadb
import langchain
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import Chroma
from langchain.text_splitter import CharacterTextSplitter
from langchain.chat_models import ChatOpenAI
from langchain.chains import ConversationalRetrievalChain
import pdf
import llm

embeddings = OpenAIEmbeddings()
vectorstore = Chroma.from_documents(
	pdf.pages,
	embedding=embeddings,
	persist_directory=".",
	)
vectorstore.persist()

qa = ConversationalRetrievalChain.from_llm(
	llm.llm,
	vectorstore.as_retriever(),
	return_source_documents=True
	)

chat_history = []
query = input("質問文を入力してください(qで終了) : ")

result = qa({"question":query, "chat_history":chat_history})
print("回答 : ",result["answer"])

