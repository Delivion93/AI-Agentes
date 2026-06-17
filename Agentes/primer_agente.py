from datetime import datetime

from langchain.messages import HumanMessage
from langchain.tools import tool
from langchain_ollama import ChatOllama
from langchain.agents import  create_agent

MODEL = "qwen3:8b"
TEMPERATURE = 0

@tool
def get_current_time() -> str:
    """Deuelve la fecha y la hora actual em formato ISO"""
    print("Llamando la herramienta")
    return datetime.now().isoformat()

llm = ChatOllama(model=MODEL, temperature=TEMPERATURE)
agent = create_agent(llm, tools=[get_current_time])
message = HumanMessage("¿Qué hora es?")
result = agent.invoke({"messages":[message]})
for m in result["messages"]:
    print(f"[{m.type}] {m.content[:200]}")
