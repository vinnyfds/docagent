# MCP Setup Guide for DocGen Suite

## Overview

The DocGen Suite provides two MCP (Model Context Protocol) servers that integrate with Cursor IDE:

- **DocGenAgent**: Core document generation tools
- **DocGenOrchestrator**: Profile-based orchestration tools

## Installation Status ✅

- ✅ fastmcp and mcp packages installed
- ✅ Both MCP servers configured and working
- ✅ FastMCP v2 API compatibility confirmed
- ✅ Global MCP configuration updated

## Cursor Configuration

The global MCP configuration at `c:\Users\kvnr\.cursor\mcp.json` is configured with:

```json
{
  "mcpServers": {
    "DocGenAgent": {
      "command": "C:\\Users\\kvnr\\AppData\\Local\\Programs\\Python\\Python310\\python.exe",
      "args": ["D:\\langgraph agents\\docs_agent\\server.py"],
      "cwd": "D:\\langgraph agents"
    },
    "DocGenOrchestrator": {
      "command": "C:\\Users\\kvnr\\AppData\\Local\\Programs\\Python\\Python310\\python.exe",
      "args": ["D:\\langgraph agents\\orchestrator\\server.py"],
      "cwd": "D:\\langgraph agents"
    }
  }
}
```

## Setup Steps

### 1. Restart Cursor

- Close and reopen Cursor to load the new MCP configuration
- Check the Output panel for MCP server connection messages

### 2. Verify MCP Tools

In Cursor, you should now have access to:

**DocGenAgent Tools:**

- `ping()` - Health check
- `list_tools()` - List available tools
- `generate_documents(idea_json, docs, overwrite)` - Generate specific documents
- `generate_all(idea_json, overwrite)` - Generate all documents
- `list_outputs()` - List generated outputs
- `show_doc(path)` - Show document content
- `zip_outputs()` - Create zip of all outputs

**DocGenOrchestrator Tools:**

- `ping()` - Health check
- `list_tools()` - List available tools
- `orchestrate_docgen(idea_json, profile, overwrite)` - Orchestrate with profiles

### 3. Test MCP Integration

1. Open a new file in Cursor
2. Type `/` to see available commands
3. Look for DocGen tools in the command palette
4. Test with `ping()` to verify connectivity

## Troubleshooting

### MCP Servers Not Loading

- Check that Python paths in global MCP config are correct
- Verify fastmcp is installed: `pip install fastmcp`
- Check Cursor Output panel for error messages
- Ensure working directory (`cwd`) is set to project root

### Import Errors

- Ensure you're in the project root directory
- Verify all dependencies are installed: `pip install -r requirements.txt`
- Check that `sys.path.insert` is working in server files

### Template Errors

- Run verification: `python scripts/verify_mcp.py`
- Check template syntax in `docs_agent/prompts/`
- Verify sample data structure in `tests/fixtures/idea_sample.json`

## Usage Examples

### Generate All Documents

```python
# In Cursor MCP tool
idea_json = '{"title": "My Project", "description": "Project description", ...}'
result = generate_all(idea_json, overwrite=False)
```

### Generate Specific Documents

```python
docs = ["brd_prd", "frd", "srd"]
result = generate_documents(idea_json, docs, overwrite=False)
```

### Use Orchestrator Profiles

```python
profiles = ["full", "lean", "tech_only", "pm_only"]
result = orchestrate_docgen(idea_json, profile="lean", overwrite=False)
```

## Next Steps

- Test MCP tools in Cursor
- Generate documents using the IDE integration
- Verify tool registration in MCP Servers panel
- Check Output → MCP Logs for server activity

## Support

If you encounter issues:

1. Check the verification script: `python scripts/verify_mcp.py`
2. Review Cursor Output panel for MCP errors
3. Verify server startup: `python docs_agent/server.py`
4. Check global MCP configuration in `c:\Users\kvnr\.cursor\mcp.json`
5. Ensure working directory is set correctly in MCP config
