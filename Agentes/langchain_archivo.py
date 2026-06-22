from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_ollama import OllamaEmbeddings
from langchain_chroma import Chroma

# 1. Cargar PDF
docs = PyPDFLoader("manual.pdf").load()

# 2. Trocear en chunks de -800 caracteres

