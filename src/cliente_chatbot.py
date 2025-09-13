"""
Cliente MCP Chatbot usando LLM Claude (Anthropic)
Recibe instrucciones en lenguaje natural, consulta al LLM qué herramienta usar y llama al servidor MCP
"""

import os
import uuid
import requests
import json
from anthropic import Anthropic
from dotenv import load_dotenv
load_dotenv()

# ✅ API KEY de Claude
ANTHROPIC_API_KEY = os.getenv("ANTHROPIC_API_KEY")
anthropic = Anthropic(api_key=ANTHROPIC_API_KEY)

# URL del servidor MCP local
MCP_SERVER_URL = "http://localhost:5000/jsonrpc"

# Archivo de log
LOG_FILE = "mcp_log.txt"

# Prompt inicial del sistema
SYSTEM_PROMPT = """
Eres un agente MCP que puede utilizar herramientas expuestas por un servidor MCP.
Cuando el usuario diga algo, debes seleccionar el nombre de la herramienta a usar
y los parámetros necesarios. Tu respuesta debe estar en formato JSON, por ejemplo:

{
  "tool_name": "add_task",
  "parameters": {
    "nombre": "Estudiar redes",
    "duracion": 120,
    "deadline": "2025-09-20T23:59",
    "prioridad": "alta",
    "categoria": "universidad"
  }
}

Si el usuario quiere ver las tareas, responde con:
{
  "tool_name": "list_tasks",
  "parameters": {}
}
"""

# ▶ Función para consultar a Claude
def interpretar_instruccion_usuario(texto_usuario):
    try:
        completion = anthropic.messages.create(
            model="claude-sonnet-4-20250514",
            max_tokens=500,
            system=SYSTEM_PROMPT,
            messages=[
                {"role": "user", "content": texto_usuario}
            ]
        )

        respuesta_raw = completion.content[0].text.strip()

        # 🧹 Limpiar bloque de código si viene con ```json ... ```
        if respuesta_raw.startswith("```json"):
            respuesta_raw = respuesta_raw.removeprefix("```json").removesuffix("```").strip()
        elif respuesta_raw.startswith("```"):
            respuesta_raw = respuesta_raw.removeprefix("```").removesuffix("```").strip()

        respuesta_json = json.loads(respuesta_raw)
        return respuesta_json

    except Exception as e:
        print("❌ Error interpretando respuesta del LLM o llamando a Claude:")
        print(e)
        return None

# ▶ Función para hacer llamada al servidor MCP
def llamar_herramienta(tool_name, parameters):
    payload = {
        "tool_name": tool_name,
        "tool_use_id": str(uuid.uuid4()),
        "parameters": parameters
    }

    try:
        response = requests.post(MCP_SERVER_URL, json=payload)
        guardar_log(payload, response.json())
        return response.json()
    except Exception as e:
        return {"error": str(e)}

# ▶ Guardar log de interacciones
def guardar_log(request_json, response_json):
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write("### REQUEST ###\n")
        f.write(json.dumps(request_json, indent=2, ensure_ascii=False) + "\n")
        f.write("### RESPONSE ###\n")
        f.write(json.dumps(response_json, indent=2, ensure_ascii=False) + "\n\n")

# ▶ Menú principal
def main():
    print("🤖 Chatbot Anfitrión MCP usando Claude (escribe 'salir' para terminar)")
    while True:
        entrada = input("🧑 Tú: ")
        if entrada.strip().lower() == "salir":
            break

        if not entrada.strip():
            print("⚠️ Instrucción vacía, escribe algo.")
            continue

        instruccion = interpretar_instruccion_usuario(entrada)
        if not instruccion:
            print("⚠️ No entendí la instrucción.")
            continue

        tool_name = instruccion.get("tool_name")
        params = instruccion.get("parameters", {})

        print(f"🔧 Llamando herramienta: {tool_name} con parámetros: {params}")
        resultado = llamar_herramienta(tool_name, params)

        print(" Respuesta:")
        print(json.dumps(resultado, indent=2, ensure_ascii=False))

if __name__ == "__main__":
    main()
