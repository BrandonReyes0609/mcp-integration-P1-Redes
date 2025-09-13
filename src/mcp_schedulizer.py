"""
Servidor MCP Schedulizer - Compatible con protocolo MCP 2025
Expone herramientas bajo JSON-RPC y /tools/definition.json
"""

from flask import Flask, request, jsonify, send_from_directory
import uuid
import os
import datetime
import json

app = Flask(__name__)

# In-memory database
tasks = []
calendar = []

# Ruta para servir el archivo tools/definition.json
@app.route('/tools/definition.json', methods=['GET'])
def get_definition():
    return send_from_directory('tools', 'definition.json')

# MCP JSON-RPC handler
@app.route('/jsonrpc', methods=['POST'])
def handle_jsonrpc():
    try:
        data = request.get_json()

        if "tool_name" not in data or "parameters" not in data:
            return jsonify({
                "error": {
                    "code": -32600,
                    "message": "Invalid MCP call. 'tool_name' and 'parameters' required"
                }
            }), 400

        tool_name = data["tool_name"]
        params = data["parameters"]
        tool_use_id = data.get("tool_use_id", str(uuid.uuid4()))

        if tool_name == "add_task":
            return handle_add_task(params, tool_use_id)
        elif tool_name == "remove_task":
            return handle_remove_task(params, tool_use_id)
        elif tool_name == "list_tasks":
            return handle_list_tasks(tool_use_id)
        elif tool_name == "generate_schedule":
            return handle_generate_schedule(params, tool_use_id)
        elif tool_name == "get_calendar":
            return handle_get_calendar(tool_use_id)
        else:
            return jsonify({
                "error": {
                    "code": -32001,
                    "message": "tool_not_found"
                }
            }), 404

    except Exception as e:
        return jsonify({
            "error": {
                "code": -32099,
                "message": "internal_server_error",
                "data": str(e)
            }
        }), 500

# 🧩 Funciones de herramientas

def handle_add_task(params, tool_use_id):
    required = ["nombre", "duracion", "deadline", "prioridad", "categoria"]
    if not all(k in params for k in required):
        return jsonify({
            "error": {
                "code": -32602,
                "message": "invalid_params",
                "data": f"Missing fields: {', '.join(k for k in required if k not in params)}"
            }
        }), 400

    tasks.append(params)
    return jsonify({
        "tool_use_id": tool_use_id,
        "result": {
            "status": "tarea agregada correctamente",
            "tareas_totales": len(tasks)
        }
    })

def handle_remove_task(params, tool_use_id):
    nombre = params.get("nombre")
    global tasks
    tasks = [t for t in tasks if t["nombre"] != nombre]
    return jsonify({
        "tool_use_id": tool_use_id,
        "result": {"status": f"tarea '{nombre}' eliminada"}
    })

def handle_list_tasks(tool_use_id):
    return jsonify({
        "tool_use_id": tool_use_id,
        "result": {"tasks": tasks}
    })

def handle_generate_schedule(params, tool_use_id):
    # Simulación básica
    global calendar
    calendar = []
    fecha_inicio = datetime.datetime.fromisoformat(params["fecha_inicio"])
    for i, task in enumerate(tasks):
        bloque = {
            "fecha": (fecha_inicio + datetime.timedelta(days=i)).strftime("%Y-%m-%d"),
            "inicio": "09:00",
            "fin": "11:00",
            "nombre": task["nombre"]
        }
        calendar.append(bloque)
    return jsonify({
        "tool_use_id": tool_use_id,
        "result": {"calendar": calendar}
    })

def handle_get_calendar(tool_use_id):
    return jsonify({
        "tool_use_id": tool_use_id,
        "result": {"calendar": calendar}
    })

if __name__ == '__main__':
    app.run(port=5000)
