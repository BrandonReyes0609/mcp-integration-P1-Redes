# 🤖 README_LLM.md – Cliente Anfitrión MCP con Claude

Este documento describe el funcionamiento del agente anfitrión desarrollado para el **Proyecto 1 - Uso de un protocolo existente (CC3067)**, el cual utiliza un **LLM (Claude)** para interpretar instrucciones en lenguaje natural y ejecutar herramientas a través de un **servidor MCP local** compatible con el protocolo oficial.

---

## 🧠 ¿Qué hace este agente?

- Actúa como **cliente anfitrión MCP**.
- Se comunica con **Claude Sonnet 4** usando el SDK oficial de Anthropic.
- Interpreta lo que escribe el usuario (en español).
- Genera un bloque JSON válido con:
  - `tool_name`: nombre de la herramienta a invocar
  - `parameters`: parámetros necesarios
- Llama automáticamente al **servidor MCP local** con ese JSON.
- Muestra la respuesta al usuario.

---

## 🔧 Herramientas disponibles

El LLM puede usar herramientas como:

| Herramienta        | Descripción                                     |
|--------------------|--------------------------------------------------|
| `add_task`         | Agrega una nueva tarea                          |
| `list_tasks`       | Muestra todas las tareas almacenadas            |
| `remove_task`      | Elimina una tarea por nombre                    |
| `generate_schedule`| Genera un horario optimizado basado en tareas   |
| `get_calendar`     | Muestra el calendario generado                  |

Estas herramientas están definidas en los archivos `.tool.json` y referenciadas desde `definition.json`.

---

## 💬 Ejemplo de conversación

### 🧑 Usuario:
```
Agrega una tarea llamada estudiar redes, que dure 2 horas, con deadline el 20 de septiembre, prioridad alta, categoría universidad.
```

### 🤖 Claude (respuesta del LLM):
```json
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
```

### 📡 Cliente MCP:
Envía ese JSON al servidor MCP local (`POST /jsonrpc`).

### 📥 Respuesta del servidor:
```json
{
  "tool_use_id": "xyz-123",
  "result": {
    "status": "tarea agregada correctamente",
    "tareas_totales": 1
  }
}
```

---

## 🗂 Archivos involucrados

| Archivo                  | Descripción |
|--------------------------|-------------|
| `cliente_chatbot.py`     | Código principal del chatbot que usa Claude |
| `mcp_schedulizer.py`     | Servidor MCP con herramientas registradas |
| `tools/definition.json`  | Definición de las herramientas MCP |
| `add_task.tool.json` etc | Especificación de cada herramienta |
| `mcp_log.txt`            | Registro de todas las llamadas JSON-RPC |

---

## ✅ Requisitos previos

- Python 3.10+
- Librerías: `anthropic`, `requests`, `flask`
- API Key válida de Anthropic
- Servidor MCP corriendo en `http://localhost:5000`

---

## 📌 Notas

- Este agente **no usa menús**, actúa como un LLM natural conversacional.
- Claude debe responder exactamente con JSON válido, por lo que se implementó un sistema de limpieza de ```json ... ``` en la respuesta del modelo.