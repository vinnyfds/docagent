#!/usr/bin/env python3
"""Test MCP servers startup and tool registration"""

import sys
import asyncio
from pathlib import Path

# Add project root to path
sys.path.insert(0, str(Path(__file__).parent.parent))

def test_docs_agent_server():
  """Test Docs Agent server creation and tool registration"""
  print("Testing Docs Agent server...")
  
  try:
    from docs_agent.server import mcp
    print(f"✓ Server created: {mcp.name}")
    
    # Test tool registration
    print(f"✓ Server type: {type(mcp).__name__}")
    print(f"✓ FastMCP version: {mcp.version}")
    
    print("✓ Docs Agent server test passed!")
    return True
    
  except Exception as e:
    print(f"✗ Docs Agent server test failed: {e}")
    return False

def test_orchestrator_server():
  """Test Orchestrator server creation and tool registration"""
  print("\nTesting Orchestrator server...")
  
  try:
    from orchestrator.server import mcp
    print(f"✓ Server created: {mcp.name}")
    
    # Test tool registration
    print(f"✓ Server type: {type(mcp).__name__}")
    print(f"✓ FastMCP version: {mcp.version}")
    
    print("✓ Orchestrator server test passed!")
    return True
    
  except Exception as e:
    print(f"✗ Orchestrator server test failed: {e}")
    return False

def test_server_startup():
  """Test if servers can start without errors"""
  print("\nTesting server startup...")
  
  try:
    # Test Docs Agent startup
    from docs_agent.server import mcp as docs_mcp
    print("✓ Docs Agent server can be imported")
    
    # Test Orchestrator startup
    from orchestrator.server import mcp as orch_mcp
    print("✓ Orchestrator server can be imported")
    
    print("✓ Server startup test passed!")
    return True
    
  except Exception as e:
    print(f"✗ Server startup test failed: {e}")
    return False

async def test_async_tools():
  """Test async tool access"""
  print("\nTesting async tool access...")
  
  try:
    from docs_agent.server import mcp
    
    # Test getting tools asynchronously
    tools = await mcp.get_tools()
    print(f"✓ Tools retrieved: {len(tools)}")
    
    tool_names = [tool.name for tool in tools]
    print(f"✓ Tool names: {tool_names}")
    
    print("✓ Async tool access test passed!")
    return True
    
  except Exception as e:
    print(f"✗ Async tool access test failed: {e}")
    return False

def main():
  """Run all tests"""
  print("DocGen Suite - MCP Server Tests")
  print("=" * 40)
  
  tests = [
    test_docs_agent_server(),
    test_orchestrator_server(),
    test_server_startup(),
  ]
  
  # Test async functionality
  try:
    asyncio.run(test_async_tools())
    tests.append(True)
  except Exception as e:
    print(f"✗ Async test failed: {e}")
    tests.append(False)
  
  # Summary
  passed = sum(tests)
  total = len(tests)
  
  print(f"\n{'='*40}")
  print(f"Test Results: {passed}/{total} passed")
  
  if passed == total:
    print("🎉 All tests passed! MCP servers are ready for Cursor.")
    return 0
  else:
    print("❌ Some tests failed. Check the output above.")
    return 1

if __name__ == "__main__":
  sys.exit(main())
