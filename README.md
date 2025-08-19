# DocAgent - AI-Powered Document Generation Suite

[![Python](https://img.shields.io/badge/Python-3.9+-blue.svg)](https://python.org)
[![FastMCP](https://img.shields.io/badge/FastMCP-2.11.3-green.svg)](https://gofastmcp.com)
[![LangGraph](https://img.shields.io/badge/LangGraph-Latest-orange.svg)](https://github.com/langchain-ai/langgraph)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

> **AI-powered document generation suite with LangGraph workflows and Cursor IDE integration via MCP (Model Context Protocol)**

DocAgent is a comprehensive document generation system that creates professional software documentation using AI. It integrates seamlessly with Cursor IDE through MCP servers and supports 12 different document types with orchestrated workflows.

## 🚀 Features

### Document Types
- **📋 Business Requirements (BRD/PRD)** - Product and business requirement documents
- **⚙️ Functional Requirements (FRD)** - Detailed functional specifications
- **🏗️ System Requirements (SRD)** - System architecture and requirements
- **🧪 Technical Requirements (TRD/TDD)** - Technical design and test documents
- **🗄️ Database Design (ERD/API)** - Entity relationship diagrams and API specs
- **🎨 UI/UX Design** - Wireframes and design system documentation
- **📊 Project Planning** - Project plans and milestone tracking
- **✅ Test Strategy** - Comprehensive testing documentation
- **🚀 CI/CD Documentation** - Deployment and environment setup
- **📦 Release Runbooks** - Release procedures and rollback plans

### Core Capabilities
- **🔄 LangGraph Workflows** - Parallel document generation with conditional logic
- **🎯 Smart Orchestration** - Profile-based generation (Full, Lean, Tech-only, PM-only)
- **💻 Cursor IDE Integration** - Native MCP server integration
- **🛡️ Safe File Operations** - Collision detection and backup systems
- **📝 Jinja2 Templates** - Customizable document templates
- **⚡ FastMCP v2** - Modern MCP protocol implementation
- **🔧 CLI Tools** - Command-line interface for batch operations

## 📦 Installation

### Prerequisites
- Python 3.9+
- Cursor IDE
- Git

### Quick Setup
```bash
# Clone the repository
git clone https://github.com/vinnyfds/docagent.git
cd docagent

# Install dependencies
pip install -r requirements.txt

# Create environment file
cp .env.template .env
# Edit .env with your API keys

# Verify installation
python scripts/verify_mcp.py
```

### Cursor IDE Integration
```bash
# Install FastMCP
pip install fastmcp

# The MCP servers will be automatically configured in Cursor
# Restart Cursor to load the DocAgent tools
```

## 🎯 Quick Start

### Using Cursor IDE (Recommended)
1. Open any file in Cursor
2. Type `/` to open command palette
3. Look for DocAgent tools:
   - `ping()` - Health check
   - `generate_all()` - Generate all documents
   - `orchestrate_docgen()` - Profile-based generation

### Using CLI
```bash
# Generate all documents
python scripts/cli_generate.py --idea tests/fixtures/idea_sample.json --all

# Generate specific documents
python scripts/cli_generate.py --idea my_idea.json --docs brd_prd frd srd

# Use orchestration profiles
python -c "
from orchestrator.graph import orchestrate_docgen
from docs_agent.state import Idea
import json

with open('tests/fixtures/idea_sample.json') as f:
    data = json.load(f)
    idea = Idea(**data)
    
result = orchestrate_docgen(idea, profile='lean', overwrite=False)
print('Generated:', result)
"
```

## 🏗️ Architecture

### System Overview
```
┌─────────────────┐    ┌──────────────────┐    ┌─────────────────┐
│   Cursor IDE    │◄──►│  FastMCP Server  │◄──►│  LangGraph      │
│                 │    │                  │    │  Workflow       │
│ - Command Palette│    │ - DocGenAgent    │    │                 │
│ - Tools Integration │  │ - Orchestrator   │    │ - Parallel Nodes│
│ - MCP Protocol  │    │ - Tool Registry  │    │ - Conditional   │
└─────────────────┘    └──────────────────┘    └─────────────────┘
                                │
                                ▼
                       ┌──────────────────┐
                       │  Document Engine │
                       │                  │
                       │ - Jinja2 Templates│
                       │ - Safe File Ops  │
                       │ - Output Manager │
                       └──────────────────┘
```

### Project Structure
```
docagent/
├── docs_agent/              # Core document generation agent
│   ├── __init__.py         # Package initialization
│   ├── state.py            # Pydantic models (Idea, Context, DocRequest)
│   ├── graph.py            # LangGraph workflow definition
│   ├── server.py           # FastMCP server implementation
│   ├── nodes/              # Document generation nodes
│   │   ├── brd_prd.py      # Business requirements
│   │   ├── frd.py          # Functional requirements
│   │   ├── srd.py          # System requirements
│   │   └── ...             # Other document types
│   ├── prompts/            # Jinja2 templates
│   │   ├── brd_prd.md.jinja
│   │   ├── openapi.yaml.jinja
│   │   └── ...
│   └── utils/              # Utilities
│       ├── render.py       # Template rendering
│       └── safety.py       # Safe file operations
├── orchestrator/           # Orchestration layer
│   ├── graph.py            # Orchestration logic
│   └── server.py           # Orchestrator MCP server
├── scripts/                # CLI and utilities
│   ├── cli_generate.py     # Command-line interface
│   ├── verify_mcp.py       # Installation verification
│   └── test_mcp_servers.py # Server testing
├── tests/                  # Test suite
│   └── fixtures/           # Test data
│       └── idea_sample.json
├── outputs/                # Generated documents
├── .cursor_rules           # Cursor IDE guardrails
├── requirements.txt        # Python dependencies
├── .env.template          # Environment template
└── README.md              # This file
```

## 🎮 Usage Examples

### Idea Structure
```json
{
  "title": "E-commerce Platform",
  "description": "Modern e-commerce platform with AI recommendations",
  "context": {
    "domain": "E-commerce",
    "stakeholders": ["Product Manager", "Engineering Team", "UX Designer"],
    "timeline": "6 months",
    "budget": "$500K"
  },
  "personas": [
    {"name": "Customer", "description": "Online shoppers"},
    {"name": "Admin", "description": "Platform administrators"}
  ],
  "modules": [
    {"name": "User Management", "description": "User registration and profiles"},
    {"name": "Product Catalog", "description": "Product browsing and search"},
    {"name": "Shopping Cart", "description": "Cart and checkout functionality"}
  ],
  "entities": [
    {"name": "User", "fields": ["id", "email", "profile"]},
    {"name": "Product", "fields": ["id", "name", "price", "inventory"]}
  ],
  "apis": [
    {"name": "User API", "methods": ["GET", "POST", "PUT", "DELETE"]},
    {"name": "Product API", "methods": ["GET", "POST", "PUT"]}
  ]
}
```

### Orchestration Profiles
```python
PROFILES = {
    "full": [
        "brd_prd", "frd", "srd", "trd_tdd", "erd_api", 
        "ui_wireframes", "project_plan", "test_strategy", 
        "cicd_env", "release_runbook"
    ],
    "lean": ["brd_prd", "frd", "srd", "erd_api"],
    "tech_only": ["srd", "trd_tdd", "erd_api", "cicd_env"],
    "pm_only": ["brd_prd", "project_plan", "test_strategy", "release_runbook"]
}
```

## 🛠️ Development

### Running Tests
```bash
# Run verification tests
python scripts/verify_mcp.py

# Test MCP servers
python scripts/test_mcp_servers.py

# Generate sample documents
python scripts/cli_generate.py --idea tests/fixtures/idea_sample.json --all
```

### Code Quality
```bash
# Install development dependencies
pip install ruff pytest

# Run linting
ruff check .

# Run tests
pytest -v
```

### Contributing
1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 🔧 Configuration

### Environment Variables
```bash
# Required
OPENAI_API_KEY=your_openai_api_key_here

# Optional
DOCGEN_BUCKET=your_s3_bucket_for_outputs
ALLOW_OVERWRITE=false
LOG_LEVEL=INFO
ENVIRONMENT=development
MCP_HOST=localhost
MCP_PORT=3000
```

### Cursor MCP Setup
The MCP servers are automatically configured for Cursor IDE. Manual configuration:

```json
{
  "mcpServers": {
    "DocGenAgent": {
      "command": "cmd",
      "args": ["/c", "python", "docs_agent/server.py"],
      "cwd": "/path/to/docagent"
    },
    "DocGenOrchestrator": {
      "command": "cmd", 
      "args": ["/c", "python", "orchestrator/server.py"],
      "cwd": "/path/to/docagent"
    }
  }
}
```

## 📚 Documentation

- [Installation Guide](docs/installation.md)
- [MCP Setup Guide](MCP_SETUP.md)
- [Template Customization](docs/templates.md)
- [AWS Deployment](docs/aws-deployment.md)
- [API Reference](docs/api-reference.md)

## 🚀 Deployment

### AWS Lambda (Coming Soon)
```bash
# Package for serverless deployment
npm install -g serverless
serverless deploy
```

### Docker
```bash
# Build container
docker build -t docagent .

# Run container
docker run -p 3000:3000 docagent
```

## 🤝 Contributing

We welcome contributions! Please see our [Contributing Guide](CONTRIBUTING.md) for details.

### Contributors
- [@vinnyfds](https://github.com/vinnyfds) - Creator & Maintainer

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- [LangGraph](https://github.com/langchain-ai/langgraph) - Workflow orchestration
- [FastMCP](https://gofastmcp.com) - MCP server framework
- [Cursor IDE](https://cursor.com) - AI-powered development environment
- [Jinja2](https://jinja.palletsprojects.com/) - Template engine

## 📧 Support

- **Issues**: [GitHub Issues](https://github.com/vinnyfds/docagent/issues)
- **Discussions**: [GitHub Discussions](https://github.com/vinnyfds/docagent/discussions)
- **Email**: vinnyfds@gmail.com

---

**🎯 Transform your ideas into comprehensive documentation with AI-powered precision!**
