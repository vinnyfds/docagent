"""Orchestrator MCP server for DocGen Suite"""

import sys
from pathlib import Path
from typing import Dict, Any, List

# Add project root to path
sys.path.insert(0, str(Path(__file__).parent.parent))

from fastmcp import FastMCP
from docs_agent.state import Idea
from orchestrator.graph import orchestrate_docgen


def get_output_directory() -> Path:
  """Get the appropriate output directory, creating it if necessary"""
  # Try multiple possible locations in order of preference
  possible_paths = [
    # 1. Relative to current working directory
    Path.cwd() / "docs_agent" / "outputs",
    # 2. Relative to script location
    Path(__file__).parent.parent / "docs_agent" / "outputs",
    # 3. In current working directory
    Path.cwd() / "outputs",
    # 4. In user's home directory as fallback
    Path.home() / "docgen_outputs"
  ]
  
  for path in possible_paths:
    try:
      # Create directory if it doesn't exist
      path.mkdir(parents=True, exist_ok=True)
      # Test if we can write to it
      test_file = path / ".test_write"
      test_file.write_text("test", encoding="utf-8")
      test_file.unlink()  # Clean up test file
      return path
    except (OSError, PermissionError):
      continue
  
  # If all else fails, use current working directory
  fallback_path = Path.cwd() / "docgen_outputs"
  fallback_path.mkdir(parents=True, exist_ok=True)
  return fallback_path

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
    # Set the output directory to the one we can actually write to
    idea.output_dir = get_output_directory()
    result = orchestrate_docgen(idea, profile, overwrite)
    return {"success": True, "result": result}
  except Exception as e:
    return {"success": False, "error": str(e)}


if __name__ == "__main__":
  mcp.run()
