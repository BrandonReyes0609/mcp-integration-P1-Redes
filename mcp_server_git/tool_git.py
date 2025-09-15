import subprocess
from mcp import Tool
from pydantic import Field

class GitTool(Tool):
    # Campos obligatorios de MCP Tool
    name: str = Field(default="git", description="Herramientas para manejar un repositorio Git")
    description: str = Field(default="Provee comandos básicos de Git (status, log)")
    inputSchema: dict = Field(default_factory=lambda: {"type": "object", "properties": {}})

    # Campo personalizado para la ruta del repo
    repo_path: str = Field(..., description="Ruta al repositorio Git")

    def list_tools(self):
        """Lista las herramientas disponibles en este servidor."""
        return [
            {
                "name": "status",
                "description": "Muestra el estado del repositorio Git",
                "input_schema": {"type": "object", "properties": {}}
            },
            {
                "name": "log",
                "description": "Muestra el historial de commits en formato corto",
                "input_schema": {"type": "object", "properties": {}}
            }
        ]

    def call_tool(self, tool_name, arguments):
        """Ejecuta la herramienta seleccionada en el repositorio Git."""
        if tool_name == "status":
            return subprocess.run(
                ["git", "-C", self.repo_path, "status"],
                capture_output=True,
                text=True
            ).stdout

        elif tool_name == "log":
            return subprocess.run(
                ["git", "-C", self.repo_path, "log", "--oneline", "--decorate"],
                capture_output=True,
                text=True
            ).stdout

        return f"Herramienta desconocida: {tool_name}"
