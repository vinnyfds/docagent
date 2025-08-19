"""TRD/TDD document generation node"""

from pathlib import Path
from typing import Dict, Any
from ..state import Idea
from ..utils.render import render_template
from ..utils.safety import safe_write


def generate_trd_tdd(state: Idea) -> Dict[str, Any]:
  """Generate TRD/TDD document"""
  content = render_template("trd_tdd.md.jinja", {"idea": state})
  dest_dir = state.output_dir
  output_path = dest_dir / "trd_tdd.md"
  final_path = safe_write(output_path, content, state.overwrite or False)
  return {
    "name": "TRD/TDD",
    "path": str(final_path),
    "type": "markdown",
    "template": "trd_tdd.md.jinja"
  }
