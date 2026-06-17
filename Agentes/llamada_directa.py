import requests



response = requests.post(
    url="http://localhost:11434/api/chat",
    json={
        "model": "qwen3:8b",
        "messages": [
            {
                "role": "user",
                "content": "Explica RAG en una frase."
            }
        ],
        "stream": False,
    },
)

contenido = response.json()

print(contenido["message"]["content"])