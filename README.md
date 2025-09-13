# 🚀 MCP-Schedulizer Integration – Project 1 (Delivery 2)

## 🎯 Project Purpose

This repository contains the **second delivery** of Project 1 for the course **CC3067 – Computer Networks (UVG)**.
It extends the **MCP-Schedulizer local server** by integrating multiple MCP servers, a connection to an LLM API (Claude), remote deployment, and network analysis using Wireshark.

---

## 📚 Project Theme

The goal of this delivery is to **implement an existing protocol (JSON-RPC 2.0)** in different contexts:

- Local MCP server (MCP-Schedulizer).
- Integration with official MCP servers (Filesystem, Git).
- Use of other students' MCP servers.
- Remote MCP server deployment in the cloud.
- Protocol analysis with Wireshark.

---

## 🌐 Protocols Used

- **JSON-RPC 2.0** → application layer protocol for remote procedure calls.
- **HTTP POST** → transport mechanism.
- **MCP (Model Context Protocol)** → specification alignment.

---

## ⚙️ Project Structure

```
mcp-integration-P1-Redes/
│
├── src/
│   ├── cliente_chatbot.py     # Host chatbot (Claude + MCP + logs)
│   ├── mcp_schedulizer.py     # Local MCP server
│   ├── remote_server.py       # Trivial remote MCP server (cloud)
│   └── utils/                 # Utilities (logs, context management)
│
├── data/
│   ├── tasks_db.json
│   ├── agenda_exportada.csv
│   └── mcp_log.txt
│
├── docs/
│   ├── WIRESHARK_REPORT.md    # Network analysis with Wireshark
│   └── screenshots/           # Execution and capture images
│
├── tests/
│   ├── test_schedulizer.py
│   ├── test_integration.py
│
├── requirements.txt           # Python dependencies
└── .gitignore                 # Git ignore rules
```

```
mcp-schedulizer-integration-P1-Redes/
│
├── src/                         # Código fuente principal
│   ├── cliente_chatbot.py        # Host chatbot (extendido con Claude, log, etc.)
│   ├── mcp_schedulizer.py        # Tu servidor MCP local
│   ├── remote_server.py          # Servidor remoto trivial para nube
│   └── utils/                    # Funciones auxiliares (logs, contexto, etc.)
│
├── data/
│   ├── tasks_db.json             # Base de datos de tareas
│   ├── agenda_exportada.csv      # Exportación de agenda
│   └── logs/                     # Carpeta de logs MCP
│
├── docs/
│   ├── README.md                 # Instrucciones principales (en inglés)
│   ├── README_ES.md              # Opcional: versión en español
│   ├── WIRESHARK_REPORT.md       # Explicación análisis de red
│   └── screenshots/              # Capturas de Wireshark, ejecución, etc.
│
├── tests/
│   ├── test_schedulizer.py       # Pruebas unitarias de tu servidor
│   ├── test_integration.py       # Pruebas de integración con otros servidores MCP
│
├── requirements.txt              # Dependencias Python
├── .gitignore                    # Ignorar __pycache__, .env, etc.
└── LICENSE (opcional)            # Si lo haces público

```


```
mcp-schedulizer-integration-P1-Redes/
│
├── src/                         # Código fuente principal
│   ├── cliente_chatbot.py        # Host chatbot (extendido con Claude, log, etc.)
│   ├── mcp_schedulizer.py        # Tu servidor MCP local
│   ├── remote_server.py          # Servidor remoto trivial para nube
│   └── utils/                    # Funciones auxiliares (logs, contexto, etc.)
│
├── data/
│   ├── tasks_db.json             # Base de datos de tareas
│   ├── agenda_exportada.csv      # Exportación de agenda
│   └── logs/                     # Carpeta de logs MCP
│
├── docs/
│   ├── README.md                 # Instrucciones principales (en inglés)
│   ├── README_ES.md              # Opcional: versión en español
│   ├── WIRESHARK_REPORT.md       # Explicación análisis de red
│   └── screenshots/              # Capturas de Wireshark, ejecución, etc.
│
├── tests/
│   ├── test_schedulizer.py       # Pruebas unitarias de tu servidor
│   ├── test_integration.py       # Pruebas de integración con otros servidores MCP
│
├── requirements.txt              # Dependencias Python
├── .gitignore                    # Ignorar __pycache__, .env, etc.
└── LICENSE (opcional)            # Si lo haces público
```


```
/src
 ├── cliente_chatbot.py     # Chatbot anfitrión extendido (Claude + MCP + Logs)
 ├── mcp_schedulizer.py     # Tu servidor MCP local
 ├── remote_server.py       # Servidor MCP remoto trivial (Entrega 2)
 └── utils/
      ├── log_utils.py      # Función para guardar logs
      └── context_utils.py  # Manejo de contexto
```

---

## 🔹 Work Phases

### Phase 1 – Extend the Host Chatbot

- Connect Claude API.
- Manage conversation context.
- Log all MCP interactions.

### Phase 2 – Integration with Official MCP Servers

- Filesystem MCP (file creation).
- Git MCP (create repo, README, commit).

### Phase 3 – Expand MCP Ecosystem

- Integrate at least **2 classmates' MCP servers**.
- Build combined scenarios with Schedulizer.

### Phase 4 – Remote Server and Network Analysis

- Deploy `remote_server.py` to Google Cloud Run (or similar).
- Capture traffic with Wireshark.
- Classify `sync`, `request`, and `response` messages.

### Phase 5 – Documentation and Final Delivery

- Write final report with specifications.
- Include Wireshark captures and OSI layer explanations.
- Present the project in class.

---

## 🛠️ Installation

1. Clone the repository:

```bash
git clone <REPO_URL>
cd mcp-integration-P1-Redes
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

---

## ▶️ Execution

### 1. Run the local MCP server

```bash
python src/mcp_schedulizer.py
```

### 2. Run the host chatbot

```bash
python src/cliente_chatbot.py
```

### 3. Run the remote MCP server (cloud deployment)

```bash
python src/remote_server.py
```

---

## 📤 Exported Files

- `agenda_exportada.csv` → generated weekly schedule.
- `mcp_log.txt` → log of all interactions with Claude API and MCP servers.

---

## ✅ Next Steps

- Integrate Claude API connection.
- Add official MCP servers (Filesystem, Git).
- Connect classmates’ MCP servers.
- Deploy remote server and capture traffic with Wireshark.

---

📌 **Author:** Brandon Reyes Morales – Universidad del Valle de Guatemala
📌 **Course:** CC3067 – Computer Networks
