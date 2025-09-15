# Ejecuta Git MCP Server en http://localhost:8002

from mcp.servers.git.server import run

if __name__ == "__main__":
    run(host="0.0.0.0", port=8002)
