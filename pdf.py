import sys
from langchain.document_loaders import PyPDFLoader

pdf_path = 'pdf_store/' + sys.argv[1]
loader = PyPDFLoader(pdf_path)
pages = loader.load_and_split()
