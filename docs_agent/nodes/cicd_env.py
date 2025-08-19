"""CI/CD environment document generation node"""

from pathlib import Path
from typing import Dict, Any
from ..state import Idea
from ..utils.render import render_template
from ..utils.safety import safe_write


def generate_cicd_env(state: Idea) -> Dict[str, Any]:
  """Generate CI/CD environment document"""
  content = render_template("cicd_env.md.jinja", {"idea": state})
  dest_dir = state.output_dir
  output_path = dest_dir / "cicd_env.md"
  final_path = safe_write(output_path, content, state.overwrite or False)
  return {
    "name": "CI/CD Environment",
    "path": str(final_path),
    "type": "markdown",
    "template": "cicd_env.md.jinja"
  }
