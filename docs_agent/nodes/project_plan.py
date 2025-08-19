"""Project plan document generation node"""

from pathlib import Path
from typing import Dict, Any
from ..state import Idea
from ..utils.render import render_template
from ..utils.safety import safe_write


def generate_project_plan(state: Idea) -> Dict[str, Any]:
  """Generate project plan document"""
  content = render_template("project_plan.md.jinja", {"idea": state})
  dest_dir = state.output_dir
  output_path = dest_dir / "project_plan.md"
  final_path = safe_write(output_path, content, state.overwrite or False)
  return {
    "name": "Project Plan",
    "path": str(final_path),
    "type": "markdown",
    "template": "project_plan.md.jinja"
  }
