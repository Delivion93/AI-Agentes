from langchain_ollama import ChatOllama

llm = ChatOllama(model="qwen3:8b",temperature=0.2)
response = llm.invoke("Explica RAG")
print(response.content)

# temp = 0.2 RAG (Retrieval-Augmented Generation) es un metodo que combina la recuperación de información pertinente con la generación de texto para mejorar la precisión y relevancia de las respuestas de los modelos.
# temp = 0.8 RAG (Retrieval-Augmented Generation) es una técnica que combina la recuperación de información de una base de datos con la generación de texto para crear respuestas más precisas y contextualmente relevantes.
