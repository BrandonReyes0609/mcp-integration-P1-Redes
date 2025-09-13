# mcp-integration-P1-Redes

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
