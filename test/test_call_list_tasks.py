import requests

url = "http://localhost:5000/jsonrpc"

payload = {
    "tool_name": "list_tasks",
    "tool_use_id": "list-001",
    "parameters": {}
}

response = requests.post(url, json=payload)
print("Status:", response.status_code)
print("Response:", response.json())
