"""FastMCP server for DocGen Suite"""

import sys
import json
import zipfile
from pathlib import Path
from typing import Dict, Any, List

# Add project root to path
sys.path.insert(0, str(Path(__file__).parent.parent))

from fastmcp import FastMCP
from docs_agent.state import Idea
from docs_agent.graph import run_docs_generation, generate_all_documents

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
    result = run_docs_generation(idea, docs, overwrite)
    return {"success": True, "result": result}
  except Exception as e:
    return {"success": False, "error": str(e)}


@mcp.tool()
def generate_all(idea_json: str, overwrite: bool = False) -> Dict[str, Any]:
  """Generate all documents"""
  try:
    idea = Idea.model_validate_json(idea_json)
    result = generate_all_documents(idea, overwrite)
    return {"success": True, "result": result}
  except Exception as e:
    return {"success": False, "error": str(e)}


@mcp.tool()
def list_outputs() -> List[str]:
  """List generated outputs"""
  outputs_dir = Path("outputs")
  if not outputs_dir.exists():
    return []
  
  files = []
  for file_path in outputs_dir.rglob("*"):
    if file_path.is_file():
      files.append(str(file_path.relative_to(outputs_dir)))
  return files


@mcp.tool()
def show_doc(path: str) -> str:
  """Show document content"""
  try:
    doc_path = Path("outputs") / path
    if doc_path.exists():
      return doc_path.read_text(encoding="utf-8")
    return f"Document not found: {path}"
  except Exception as e:
    return f"Error reading document: {str(e)}"


@mcp.tool()
def zip_outputs() -> str:
  """Create zip of all outputs"""
  try:
    outputs_dir = Path("outputs")
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
