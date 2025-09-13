# MCP Schedulizer

This is a local MCP (Model Context Protocol) server and chatbot client implementation for the CC3067 course at Universidad del Valle de Guatemala.

## 📦 Features

- Local MCP server (`mcp_schedulizer.py`) with tools like `add_task` and `list_tasks`.
- Chatbot client (`cliente_chatbot.py`) using Anthropic Claude via API.
- Integration with **official MCP servers**: Git MCP and Filesystem MCP.
- Claude-powered natural language interaction.
- Secure `.env`-based API key management.

## 🚀 Getting Started

### 1. Clone the repo

```bash
git clone https://github.com/BrandonReyes0609/mcp-integration-P1-Redes.git
cd mcp-integration-P1-Redes
```

### 2. Create your `.env` file

```bash
cp .env.example .env
```

Then edit `.env` and paste your Anthropic API key.

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the local server

```bash
python src/mcp_schedulizer.py
```

### 5. Run the chatbot

```bash
python src/cliente_chatbot.py
```

## 🧠 Remote Deployment

To deploy the server remotely (e.g. on Google Cloud), see the folder `remote_mcp/` in this repo. Your teammate can adapt Docker and `server.py` accordingly.

## 📄 Files

- `src/mcp_schedulizer.py`: MCP server (Flask-based).
- `src/cliente_chatbot.py`: LLM client using Claude Sonnet 4.
- `tools/definition.json`: Tool definitions for this MCP server.
- `tasks_db.json`: Local persistent task store.

## 📚 Acknowledgements

- [Anthropic SDK](https://github.com/anthropics/anthropic-sdk-python)
- [Model Context Protocol](https://modelcontextprotocol.io/docs/learn/)
- Official MCP Tools: Git MCP and Filesystem MCP

---

**UVG - Redes de Computadoras - 2025**