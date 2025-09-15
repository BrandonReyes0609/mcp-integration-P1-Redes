# Ejecuta Filesystem MCP Server en http://localhost:8001

from mcp.servers.filesystem.server import run

if __name__ == "__main__":
    run(host="0.0.0.0", port=8001)
