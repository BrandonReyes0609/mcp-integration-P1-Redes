import argparse
import asyncio
from .tool_git import GitTool
from mcp import stdio_server

async def main_async():
    parser = argparse.ArgumentParser()
    parser.add_argument("--repository", required=True, help="Ruta al repositorio git")
    args = parser.parse_args()

    # Ahora instanciamos con los campos correctos
    tool = GitTool(repo_path=args.repository)

    async with stdio_server.run_stdio_server(tools=[tool]) as server:
        await server.wait_closed()

def main():
    asyncio.run(main_async())

if __name__ == "__main__":
    main()
