"""UI wireframes document generation node"""

from pathlib import Path
from typing import Dict, Any
from ..state import Idea
from ..utils.render import render_template
from ..utils.safety import safe_write


def generate_ui_wireframes(state: Idea) -> Dict[str, Any]:
  """Generate UI wireframes document"""
  content = render_template("wireframes.mmd.jinja", {"idea": state})
  dest_dir = state.output_dir
  output_path = dest_dir / "wireframes.mmd"
  final_path = safe_write(output_path, content, state.overwrite or False)
  return {
    "name": "UI Wireframes",
    "path": str(final_path),
    "type": "mermaid",
    "template": "wireframes.mmd.jinja"
  }
