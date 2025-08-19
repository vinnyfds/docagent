"""BRD/PRD document generation node"""

from pathlib import Path
from typing import Dict, Any
from ..state import Idea
from ..utils.render import render_template
from ..utils.safety import safe_write


def generate_brd_prd(state: Idea) -> Dict[str, Any]:
  """Generate BRD/PRD document"""
  content = render_template("brd_prd.md.jinja", {"idea": state})
  dest_dir = state.output_dir
  output_path = dest_dir / "brd_prd.md"
  final_path = safe_write(output_path, content, state.overwrite or False)
  return {
    "name": "BRD/PRD",
    "path": str(final_path),
    "type": "markdown",
    "template": "brd_prd.md.jinja"
  }
