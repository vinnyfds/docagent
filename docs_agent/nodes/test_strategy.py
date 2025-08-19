"""Test strategy document generation node"""

from pathlib import Path
from typing import Dict, Any
from ..state import Idea
from ..utils.render import render_template
from ..utils.safety import safe_write


def generate_test_strategy(state: Idea) -> Dict[str, Any]:
  """Generate test strategy document"""
  content = render_template("test_strategy.md.jinja", {"idea": state})
  dest_dir = state.output_dir
  output_path = dest_dir / "test_strategy.md"
  final_path = safe_write(output_path, content, state.overwrite or False)
  return {
    "name": "Test Strategy",
    "path": str(final_path),
    "type": "markdown",
    "template": "test_strategy.md.jinja"
  }
