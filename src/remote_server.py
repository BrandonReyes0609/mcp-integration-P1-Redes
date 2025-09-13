"""
Remote MCP Server
-----------------
A trivial MCP server that can be deployed to the cloud.
Implements simple methods like greet_user and get_time.
"""

from flask import Flask, request, jsonify
import datetime

app = Flask(__name__)

def greet_user(params):
    """Return a greeting message."""
    name = params.get("name", "Guest")
    return {"message": f"Hello, {name}! Welcome to the Remote MCP Server."}

def get_time(_params=None):
    """Return the current server time."""
    now = datetime.datetime.now()
    return {"server_time": now.strftime("%Y-%m-%d %H:%M:%S")}

@app.route("/", methods=["POST"])
def handle_rpc():
    """
    Handle JSON-RPC requests.
    Expected format:
    {
        "jsonrpc": "2.0",
        "method": "greet_user",
        "params": {"name": "Brandon"},
        "id": 1
    }
    """
    req = request.get_json()
    method = req.get("method")
    params = req.get("params", {})

    if method == "greet_user":
        result = greet_user(params)
    elif method == "get_time":
        result = get_time(params)
    else:
        return jsonify({"error": "Method not supported"}), 400

    return jsonify({
        "jsonrpc": "2.0",
        "result": result,
        "id": req.get("id")
    })

if __name__ == "__main__":
    # For local testing
    app.run(host="0.0.0.0", port=8080)
