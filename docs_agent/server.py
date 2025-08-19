"""FastMCP server for DocGen Suite"""

import sys
import json
import zipfile
import os
from pathlib import Path
from typing import Dict, Any, List

# Add project root to path
sys.path.insert(0, str(Path(__file__).parent.parent))

from fastmcp import FastMCP
from docs_agent.state import Idea
from docs_agent.graph import run_docs_generation, generate_all_documents


def get_output_directory() -> Path:
  """Get the appropriate output directory, creating it if necessary"""
  # Try multiple possible locations in order of preference
  possible_paths = [
    # 1. Relative to current working directory
    Path.cwd() / "docs_agent" / "outputs",
    # 2. Relative to script location
    Path(__file__).parent / "outputs",
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
mcp = FastMCP("DocGenAgent")


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
    "generate_documents",
    "generate_all",
    "list_outputs",
    "show_doc",
    "zip_outputs"
  ]


@mcp.tool()
def generate_documents(idea_json: str, docs: List[str], overwrite: bool = False) -> Dict[str, Any]:
  """Generate specific documents"""
  try:
    idea = Idea.model_validate_json(idea_json)
    # Set the output directory to the one we can actually write to
    idea.output_dir = get_output_directory()
    result = run_docs_generation(idea, docs, overwrite)
    return {"success": True, "result": result}
  except Exception as e:
    return {"success": False, "error": str(e)}


@mcp.tool()
def generate_all(idea_json: str, overwrite: bool = False) -> Dict[str, Any]:
  """Generate all documents"""
  try:
    idea = Idea.model_validate_json(idea_json)
    # Set the output directory to the one we can actually write to
    idea.output_dir = get_output_directory()
    result = generate_all_documents(idea, overwrite)
    return {"success": True, "result": result}
  except Exception as e:
    return {"success": False, "error": str(e)}


@mcp.tool()
def list_outputs() -> List[str]:
  """List generated outputs"""
  outputs_dir = get_output_directory()
  
  files = []
  for file_path in outputs_dir.rglob("*"):
    if file_path.is_file():
      files.append(str(file_path.relative_to(outputs_dir)))
  return files


@mcp.tool()
def show_doc(path: str) -> str:
  """Show document content"""
  try:
    outputs_dir = get_output_directory()
    doc_path = outputs_dir / path
    if doc_path.exists():
      return doc_path.read_text(encoding="utf-8")
    return f"Document not found: {path}"
  except Exception as e:
    return f"Error reading document: {str(e)}"


@mcp.tool()
def zip_outputs() -> str:
  """Create zip of all outputs"""
  try:
    outputs_dir = get_output_directory()
    zip_path = Path("docs_outputs.zip")
    
    with zipfile.ZipFile(zip_path, 'w') as zipf:
      for file_path in outputs_dir.rglob("*"):
        if file_path.is_file():
          zipf.write(file_path, file_path.relative_to(outputs_dir))
    
    return str(zip_path)
  except Exception as e:
    return f"Error creating zip: {str(e)}"


if __name__ == "__main__":
  mcp.run()
