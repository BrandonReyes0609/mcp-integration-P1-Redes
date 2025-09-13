# README LLM (Español)

[Click Aqui Readme LLM ESPAÑOL](docs/README_LLM_ES.md)

# 🤖 README_LLM.md – MCP Host Client with Claude Integration

This document describes the functionality of the host client developed for **Project 1 – Using an Existing Protocol (CC3067)**, which integrates a **LLM (Claude)** to interpret natural language instructions and call tools exposed by a **local MCP server** that complies with the official protocol.

---

## 🧠 What does this agent do?

- Acts as an **MCP host client**.
- Connects to **Claude Sonnet 4** using Anthropic’s official SDK.
- Interprets user instructions in natural language (Spanish or English).
- Generates valid JSON objects containing:
  - `tool_name`: name of the tool to call
  - `parameters`: input parameters for the tool
- Automatically sends that JSON to the **local MCP server**.
- Displays the server response to the user.

---

## 🔧 Available Tools

Claude can use the following tools:

| Tool Name             | Description                            |
| --------------------- | -------------------------------------- |
| `add_task`          | Adds a new task to the system          |
| `list_tasks`        | Lists all current tasks                |
| `remove_task`       | Removes a task by name                 |
| `generate_schedule` | Generates an optimized weekly schedule |
| `get_calendar`      | Displays the current calendar          |

All tools are defined in `.tool.json` files and referenced in the `definition.json` file.

---

## 💬 Sample Conversation

### 🧑 User:

```
Add a task called "study networks", lasting 2 hours, due on September 20th, high priority, category university.
```

### 🤖 Claude (LLM response):

```json
{
  "tool_name": "add_task",
  "parameters": {
    "nombre": "Study networks",
    "duracion": 120,
    "deadline": "2025-09-20T23:59",
    "prioridad": "alta",
    "categoria": "universidad"
  }
}
```

### 📡 MCP Client:

Sends the JSON to the local MCP server via POST `/jsonrpc`.

### 📥 MCP Server Response:

```json
{
  "tool_use_id": "xyz-123",
  "result": {
    "status": "task successfully added",
    "tareas_totales": 1
  }
}
```

---

## 🗂 Project Files

| File                      | Description                                          |
| ------------------------- | ---------------------------------------------------- |
| `cliente_chatbot.py`    | Main chatbot client using Claude                     |
| `mcp_schedulizer.py`    | Local MCP server with tool implementations           |
| `tools/definition.json` | Main MCP tool definition index                       |
| `add_task.tool.json`    | Individual tool schemas                              |
| `mcp_log.txt`           | Interaction log with all JSON-RPC requests/responses |

---

## ✅ Requirements

- Python 3.10+
- Libraries: `anthropic`, `requests`, `flask`
- Valid Claude API key
- Local MCP server running at `http://localhost:5000`

---

## 📌 Notes

- This agent uses **no menus** – all interactions are natural language.
- Claude must respond with valid JSON, so the client includes automatic cleanup of Markdown code blocks like ```json.
