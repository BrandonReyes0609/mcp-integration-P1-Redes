import requests

url = "http://localhost:5000/jsonrpc"

payload = {
    "tool_name": "add_task",
    "tool_use_id": "abc-123",
    "parameters": {
        "nombre": "Estudiar redes",
        "duracion": 120,
        "deadline": "2025-09-20T23:59",
        "prioridad": "alta",
        "categoria": "universidad"
    }
}

response = requests.post(url, json=payload)
print("Status:", response.status_code)
print("Response:", response.json())
