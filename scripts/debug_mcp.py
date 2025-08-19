#!/usr/bin/env python3
"""Debug MCP tool registration"""

import sys
import asyncio
from pathlib import Path

# Add project root to path
sys.path.insert(0, str(Path(__file__).parent.parent))

from fastmcp import FastMCP
from fastmcp.tools import Tool

# Create simple test server
mcp = FastMCP("DebugServer")

@mcp.tool
def simple_ping() -> str:
    """Simple ping function"""
    return "pong"

async def debug_tools():
    """Debug tool registration"""
    try:
        tools = await mcp.get_tools()
        print(f"Registered tools: {len(tools)}")
        for tool in tools:
            print(f"  - Tool type: {type(tool)}")
            print(f"  - Tool attrs: {[attr for attr in dir(tool) if not attr.startswith('_')]}")
            if hasattr(tool, 'name'):
                print(f"  - Name: {tool.name}")
            if hasattr(tool, 'description'):
                print(f"  - Description: {tool.description}")
        return tools
    except Exception as e:
        print(f"Error getting tools: {e}")
        return []

if __name__ == "__main__":
    print("Debug MCP Server")
    print("=" * 20)
    
    # Test tool registration
    result = asyncio.run(debug_tools())
    
    if result:
        print("Tools registered successfully!")
        print("Starting server...")
        mcp.run()
    else:
        print("Tool registration failed!")
