"""Orchestrator MCP server for DocGen Suite"""

import sys
from pathlib import Path
from typing import Dict, Any, List

# Add project root to path
sys.path.insert(0, str(Path(__file__).parent.parent))

from fastmcp import FastMCP
from docs_agent.state import Idea
from orchestrator.graph import orchestrate_docgen

# Create MCP server with FastMCP v2 API
mcp = FastMCP("DocGenOrchestrator")


@mcp.tool()
def ping() -> str:
  """Health check endpoint"""
  return "pong"


@mcp.tool()
def list_tools() -> List[str]:
  """List available tools"""
  return [
    "ping",
    "list_tools",
    "orchestrate_docgen"
  ]


@mcp.tool()
def orchestrate_docgen_tool(idea_json: str, profile: str = "full", overwrite: bool = False) -> Dict[str, Any]:
  """Orchestrate document generation with profile selection"""
  try:
    idea = Idea.model_validate_json(idea_json)
    result = orchestrate_docgen(idea, profile, overwrite)
    return {"success": True, "result": result}
  except Exception as e:
    return {"success": False, "error": str(e)}


if __name__ == "__main__":
  mcp.run()
