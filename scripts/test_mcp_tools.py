#!/usr/bin/env python3
"""Test MCP tools functionality"""

import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent))

from docs_agent.server import mcp as docs_mcp
from orchestrator.server import mcp as orch_mcp

def test_docs_agent():
  """Test Docs Agent MCP tools"""
  print("Testing Docs Agent MCP tools...")
  
  # Test ping
  try:
    result = docs_mcp.ping()
    print(f"✓ ping: {result}")
  except Exception as e:
    print(f"✗ ping failed: {e}")
  
  # Test list_tools
  try:
    tools = docs_mcp.list_tools()
    print(f"✓ list_tools: {tools}")
  except Exception as e:
    print(f"✗ list_tools failed: {e}")

def test_orchestrator():
  """Test Orchestrator MCP tools"""
  print("\nTesting Orchestrator MCP tools...")
  
  # Test ping
  try:
    result = orch_mcp.ping()
    print(f"✓ ping: {result}")
  except Exception as e:
    print(f"✗ ping failed: {e}")
  
  # Test list_tools
  try:
    tools = orch_mcp.list_tools()
    print(f"✓ list_tools: {tools}")
  except Exception as e:
    print(f"✗ list_tools failed: {e}")

if __name__ == "__main__":
  print("DocGen Suite - MCP Tools Test")
  print("=" * 40)
  
  test_docs_agent()
  test_orchestrator()
  
  print("\n✓ MCP tools test completed!")
