from fastapi import FastAPI
from langchain_ollama import ChatOllama



app = FastAPI()

items = {
    "1":{
        "name":"item 1","price": 10.0
    },
    "2":{
        "name":"item 2","price": 10.0
    }
}

@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: str):
    return items.get(item_id,{"message":"item not found"})

@app.get("/chat")
def read_prompt(prompt: str):
    llm = ChatOllama(model="gemma3:4b", temperature=0)
    response = llm.invoke(prompt)
    return response.content

