#!/usr/bin/env python3
"""Simple MCP server test using standard approach"""

import sys
from pathlib import Path

# Add project root to path
sys.path.insert(0, str(Path(__file__).parent.parent))

from fastmcp import FastMCP

# Create the simplest possible MCP server
app = FastMCP("SimpleTest")

@app.tool()
def ping() -> str:
    """Simple ping test"""
    return "pong"

@app.tool()
def hello(name: str) -> str:
    """Say hello to someone"""
    return f"Hello, {name}!"

if __name__ == "__main__":
    print("Starting simple MCP test server...")
    print("Tools should be registered automatically via decorators")
    app.run()
