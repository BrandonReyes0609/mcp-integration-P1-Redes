@echo off
setlocal

REM Activar entorno virtual (ajusta si tu venv tiene otro nombre o ruta)
call ".\venv_mcp\Scripts\activate.bat"

REM Abrir 1ra terminal - servidor HTTP
start "MCP Server (Flask)" cmd /k "cd src && python mcp_schedulizer.py"

REM Abrir 2da terminal - servidor Filesystem oficial
start "Filesystem Server" cmd /k "cd src && mkdir ..\workspace 2>nul && npx -y @modelcontextprotocol/server-filesystem ../workspace"

REM Abrir 3ra terminal - cliente Chatbot
start "Cliente Chatbot" cmd /k "cd src && python cliente_chatbot.py"

endlocal
