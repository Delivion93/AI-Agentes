from datetime import datetime
import random
from langchain.messages import HumanMessage
from langchain.tools import tool
from langchain_ollama import ChatOllama
from langchain.agents import create_agent

MODEL = "qwen3:8b"
TEMPERATURE = 0

@tool
def get_current_time() -> str:
    """Devuelve la feha y hora actual en formato ISO."""
    print("Llamando la herramienta")
    return datetime.now().isoformat()

@tool
def get_current_wheather() -> str:
    """Devuelve el clima actual en formato de texto."""
    print("Llamando la herramienta")
    return "Málaga, Málaga, Andalucía, Soleado, 25°C"

@tool
def get_day_of_week() -> str:
    """Devuelve el día de la semana actual en español."""
    print("Llamando la herramienta")
    dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
    return dias[datetime.now().weekday()]

@tool
def get_current_date() -> str:
    """Devuelve la fecha actual en formato legible."""
    print("Llamando la herramienta")
    return datetime.now().strftime("%d de %B de %Y")

@tool
def get_random_quote() -> str:
    """Devuelve una cita aleatoria inspiradora."""
    print("Llamando la herramienta")
    quotes = [
        "La vida es lo que sucede mientras estás ocupado haciendo otros planes. - John Lennon",
        "El único modo de hacer un gran trabajo es amar lo que haces. - Steve Jobs",
        "La innovación distingue a un líder de un seguidor. - Steve Jobs",
        "No copies a nadie excepto a la naturaleza. - Walt Disney",
        "El futuro pertenece a quienes creen en la belleza de sus sueños. - Eleanor Roosevelt"
    ]
    return random.choice(quotes)

@tool
def get_current_season() -> str:
    """Devuelve la estación actual del año."""
    print("Llamando la herramienta")
    month = datetime.now().month
    if month in [12, 1, 2]:
        return "Invierno"
    elif month in [3, 4, 5]:
        return "Primavera"
    elif month in [6, 7, 8]:
        return "Verano"
    else:
        return "Otoño"

@tool
def get_time_zone() -> str:
    """Devuelve la zona horaria actual del sistema."""
    print("Llamando la herramienta")
    import time
    if time.daylight:
        return f"Zona horaria: {time.tzname[1]}"
    else:
        return f"Zona horaria: {time.tzname[0]}"

llm = ChatOllama(model=MODEL, temperature=TEMPERATURE)
agent = create_agent(llm, tools=[get_current_time,
                                 get_current_wheather,
                                 get_day_of_week,
                                 get_current_date,
                                 get_random_quote,
                                 get_current_season,
                                 get_time_zone])
message = HumanMessage("¿Qué hora es?")
result = agent.invoke({"messages": [message]})
for m in result["messages"]:
    print(f"[{m.type}] {m.content[:200]}")