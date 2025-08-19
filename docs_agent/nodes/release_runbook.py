"""Release runbook document generation node"""

from pathlib import Path
from typing import Dict, Any
from ..state import Idea
from ..utils.render import render_template
from ..utils.safety import safe_write


def generate_release_runbook(state: Idea) -> Dict[str, Any]:
  """Generate release runbook document"""
  content = render_template("release_runbook.md.jinja", {"idea": state})
  dest_dir = state.output_dir
  output_path = dest_dir / "release_runbook.md"
  final_path = safe_write(output_path, content, state.overwrite or False)
  return {
    "name": "Release Runbook",
    "path": str(final_path),
    "type": "markdown",
    "template": "release_runbook.md.jinja"
  }
