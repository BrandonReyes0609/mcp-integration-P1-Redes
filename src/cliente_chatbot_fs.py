"""
Cliente MCP Chatbot usando Claude + Filesystem
Integra llamadas a MCP vía HTTP (tareas/calendario) y vía STDIO (filesystem).
"""

import os
import uuid
import json
import shutil
import asyncio
import requests
from pathlib import Path
from anthropic import Anthropic
from dotenv import load_dotenv
from mcp import ClientSession, stdio_client, StdioServerParameters

load_dotenv()

# === CONFIGURACIÓN ===
ANTHROPIC_API_KEY = os.getenv("ANTHROPIC_API_KEY")
anthropic = Anthropic(api_key=ANTHROPIC_API_KEY)
MCP_SERVER_URL = "http://localhost:5000/jsonrpc"  # HTTP
FS_ROOT = os.path.abspath("./workspace")          # STDIO Filesystem
LOG_FILE = "mcp_log.txt"

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

Si el usuario quiere ver tareas: {"tool_name": "list_tasks", "parameters": {}}
Si quiere leer un archivo: {"tool_name": "read_file", "parameters": {"path": "notas.txt"}}
Si quiere escribir archivo: {"tool_name": "write_file", "parameters": {"path": "nuevo.txt", "content": "Hola mundo"}}
"""

# === FUNCIONES STDIO Filesystem ===
class StdioServer:
    def __init__(self, alias: str, command: str, args: list):
        self.alias = alias
        self.params = StdioServerParameters(command=command, args=args)
        self.cm = None
        self.session = None
        self.tools = {}

    async def start(self):
        if not shutil.which(self.params.command):
            raise RuntimeError(f"{self.params.command} no está disponible en PATH.")
        self.cm = stdio_client(self.params)
        r, w = await self.cm.__aenter__()  # stream reader, writer
        self.session = await ClientSession(r, w).__aenter__()
        await self.session.initialize()

    async def stop(self):
        if self.session:
            await self.session.__aexit__(None, None, None)
        if self.cm:
            await self.cm.__aexit__(None, None, None)

    async def discover_tools(self):
        resp = await self.session.list_tools()
        for tool in resp.tools:
            self.tools[tool.name] = tool

    async def call(self, tool_name: str, params: dict):
        if tool_name not in self.tools:
            return {"error": f"Herramienta '{tool_name}' no encontrada en servidor STDIO."}

        # Crear carpeta si es escritura
        if tool_name == "write_file" and "path" in params:
            ruta_completa = Path(params["path"])
            ruta_completa.parent.mkdir(parents=True, exist_ok=True)

        resp = await self.session.call_tool(tool_name, arguments=params)
        if hasattr(resp, "model_dump"):
            return {"output": resp.model_dump()}
        return {"output": resp}

# === FUNCIONES DE CHATBOT ===

def detectar_intencion(texto: str) -> str:
    t = texto.lower()
    if any(k in t for k in ["leer archivo", "escribir", "archivo", "carpeta", "txt", ".txt", "crear archivo"]):
        return "fs"
    return "local"

def interpretar_instruccion_usuario(texto_usuario):
    try:
        completion = anthropic.messages.create(
            model="claude-sonnet-4-20250514",
            max_tokens=600,
            system=SYSTEM_PROMPT,
            messages=[{"role": "user", "content": texto_usuario}]
        )
        raw = completion.content[0].text.strip()
        if raw.startswith("```json"):
            raw = raw.removeprefix("```json").removesuffix("```").strip()
        elif raw.startswith("```"):
            raw = raw.removeprefix("```").removesuffix("```").strip()
        return json.loads(raw)
    except Exception as e:
        print("❌ Error interpretando a Claude:", e)
        return None

def ajustar_path_si_es_necesario(tool_name, params):
    if "path" in params and isinstance(params["path"], str):
        if not params["path"].startswith("workspace/"):
            params["path"] = "workspace/" + params["path"]
    return params

def llamar_herramienta_http(tool_name, parameters):
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

def guardar_log(req, resp):
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write("### REQUEST ###\n" + json.dumps(req, indent=2, ensure_ascii=False) + "\n")
        f.write("### RESPONSE ###\n" + json.dumps(resp, indent=2, ensure_ascii=False) + "\n\n")

# === MAIN LOOP ===
async def main():
    print("🤖 Chatbot MCP (Claude + Filesystem + Calendario)")
    print("Escribe 'salir' para terminar.\n")

    # Inicializar servidor STDIO Filesystem
    Path(FS_ROOT).mkdir(exist_ok=True)
    fs_server = StdioServer("fs", "npx", ["-y", "@modelcontextprotocol/server-filesystem", FS_ROOT])
    try:
        await fs_server.start()
        await fs_server.discover_tools()
        print("📂 Filesystem MCP listo.")
    except Exception as e:
        print(f"⚠️ Error iniciando Filesystem: {e}")
        fs_server = None

    # Bucle principal
    while True:
        entrada = input("🧑 Tú: ").strip()
        if entrada.lower() == "salir":
            break
        if not entrada:
            continue

        instruccion = interpretar_instruccion_usuario(entrada)
        if not instruccion:
            print("⚠️ No entendí la instrucción.")
            continue

        tool_name = instruccion.get("tool_name")
        params = instruccion.get("parameters", {})

        if not tool_name:
            print("⚠️ Instrucción sin tool_name.")
            continue

        params = ajustar_path_si_es_necesario(tool_name, params)
        print(f"🔧 Ejecutando '{tool_name}' con: {params}")
        intencion = detectar_intencion(entrada)

        if intencion == "fs" and fs_server and fs_server.session:
            resultado = await fs_server.call(tool_name, params)
        else:
            resultado = llamar_herramienta_http(tool_name, params)

        print("📬 Respuesta:")
        print(json.dumps(resultado, indent=2, ensure_ascii=False))

    # Cierre
    if fs_server:
        await fs_server.stop()

if __name__ == "__main__":
    asyncio.run(main())
