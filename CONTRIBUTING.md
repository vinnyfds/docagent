# Contributing to DocAgent

Thank you for your interest in contributing to DocAgent! This document provides guidelines and information for contributors.

## 🚀 Getting Started

### Prerequisites

- Python 3.9+
- Git
- Cursor IDE (for MCP testing)
- GitHub account

### Development Setup

1. Fork the repository on GitHub
2. Clone your fork locally:
   ```bash
   git clone https://github.com/your-username/docagent.git
   cd docagent
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   pip install ruff pytest  # Development tools
   ```
4. Set up environment:
   ```bash
   cp .env.template .env
   # Edit .env with your API keys
   ```

## 📝 Development Guidelines

### Code Style

- Follow PEP 8 guidelines
- Use 2-space indentation (project standard)
- Use type hints for all functions
- Write descriptive docstrings
- Run `ruff check .` before committing

### Commit Messages

Use [Conventional Commits](https://www.conventionalcommits.org/) format:

- `feat:` - New features
- `fix:` - Bug fixes
- `docs:` - Documentation changes
- `test:` - Adding or updating tests
- `chore:` - Maintenance tasks

Examples:

```
feat: add support for custom document templates
fix: resolve Jinja2 template syntax error in openapi.yaml
docs: update installation instructions for Windows
test: add unit tests for document generation nodes
```

### Branch Naming

- `feature/description` - New features
- `fix/description` - Bug fixes
- `docs/description` - Documentation updates
- `test/description` - Test improvements

## 🛠️ Development Workflow

### 1. Create a Feature Branch

```bash
git checkout -b feature/amazing-new-feature
```

### 2. Make Your Changes

- Write clean, well-documented code
- Add tests for new functionality
- Update documentation as needed

### 3. Test Your Changes

```bash
# Run verification tests
python scripts/verify_mcp.py

# Test MCP servers
python scripts/test_mcp_servers.py

# Run linting
ruff check .

# Run tests (when available)
pytest -v
```

### 4. Commit and Push

```bash
git add .
git commit -m "feat: add amazing new feature"
git push origin feature/amazing-new-feature
```

### 5. Create a Pull Request

- Go to GitHub and create a PR from your branch
- Provide a clear description of changes
- Link any related issues
- Wait for review and address feedback

## 📚 Contributing Areas

### High Priority

- **Test Coverage**: Add comprehensive unit tests
- **Documentation**: Improve API documentation and examples
- **Templates**: Create additional document templates
- **Error Handling**: Improve error messages and recovery

### Medium Priority

- **Performance**: Optimize document generation speed
- **CLI Improvements**: Enhance command-line interface
- **Integration Tests**: Add end-to-end testing
- **Logging**: Improve application logging

### Low Priority

- **UI/UX**: Web interface for document generation
- **Cloud Deployment**: AWS/Azure deployment guides
- **Integrations**: Additional IDE integrations
- **Internationalization**: Multi-language support

## 🔧 Technical Areas

### Document Generation

- **New Document Types**: Add support for additional document formats
- **Template Engine**: Enhance Jinja2 template capabilities
- **Output Formats**: Support for PDF, Word, etc.

### MCP Integration

- **Protocol Extensions**: Enhance MCP server functionality
- **IDE Support**: Support for additional IDEs
- **Tool Improvements**: Add new MCP tools

### LangGraph Workflows

- **Node Optimization**: Improve individual document nodes
- **Workflow Logic**: Enhance conditional routing
- **Parallel Processing**: Optimize concurrent generation

### Infrastructure

- **Packaging**: Improve installation and distribution
- **Configuration**: Enhanced configuration management
- **Monitoring**: Add health checks and metrics

## 📋 Pull Request Guidelines

### Before Submitting

- [ ] Code follows project style guidelines
- [ ] All tests pass
- [ ] Documentation is updated
- [ ] Commit messages follow conventional format
- [ ] No merge conflicts with main branch

### PR Description Template

```markdown
## Description

Brief description of changes and motivation.

## Type of Change

- [ ] Bug fix (non-breaking change which fixes an issue)
- [ ] New feature (non-breaking change which adds functionality)
- [ ] Breaking change (fix or feature that would cause existing functionality to not work as expected)
- [ ] Documentation update

## Testing

- [ ] Existing tests pass
- [ ] New tests added for new functionality
- [ ] Manual testing completed

## Checklist

- [ ] Code follows style guidelines
- [ ] Self-review completed
- [ ] Documentation updated
- [ ] No new warnings or errors
```

## 🐛 Bug Reports

### Before Reporting

1. Check existing issues for duplicates
2. Verify the bug in the latest version
3. Collect relevant system information

### Bug Report Template

```markdown
**Bug Description**
Clear description of the bug.

**Steps to Reproduce**

1. Step one
2. Step two
3. Step three

**Expected Behavior**
What should happen.

**Actual Behavior**
What actually happens.

**Environment**

- OS: [e.g. Windows 10, macOS 12]
- Python version: [e.g. 3.9.7]
- DocAgent version: [e.g. 1.0.0]
- Cursor version: [e.g. 0.42.0]

**Additional Context**
Any other relevant information.
```

## 💡 Feature Requests

### Before Requesting

1. Check existing issues and discussions
2. Consider if the feature fits the project scope
3. Think about implementation approaches

### Feature Request Template

```markdown
**Feature Description**
Clear description of the proposed feature.

**Use Case**
Describe the problem this feature would solve.

**Proposed Solution**
Your ideas for implementation.

**Alternatives Considered**
Other approaches you've considered.

**Additional Context**
Any other relevant information.
```

## 🏆 Recognition

Contributors will be recognized in:

- README.md contributors section
- GitHub releases
- Project documentation

### Types of Contributions

- **Code**: Bug fixes, features, improvements
- **Documentation**: README, guides, API docs
- **Testing**: Unit tests, integration tests
- **Design**: UI/UX, templates, graphics
- **Community**: Issue triage, discussions, support

## 📞 Getting Help

### Communication Channels

- **GitHub Issues**: Bug reports and feature requests
- **GitHub Discussions**: General questions and ideas
- **Email**: vinnyfds@gmail.com for private matters

### Response Times

- **Issues**: 1-3 business days
- **Pull Requests**: 2-5 business days
- **Discussions**: 1-2 business days

## 📄 License

By contributing to DocAgent, you agree that your contributions will be licensed under the MIT License.

---

Thank you for contributing to DocAgent! 🎉
