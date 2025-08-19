"""FRD document generation node"""

from pathlib import Path
from typing import Dict, Any
from ..state import Idea
from ..utils.render import render_template
from ..utils.safety import safe_write


def generate_frd(state: Idea) -> Dict[str, Any]:
  """Generate FRD document"""
  content = render_template("frd.md.jinja", {"idea": state})
  dest_dir = state.output_dir
  output_path = dest_dir / "frd.md"
  final_path = safe_write(output_path, content, state.overwrite or False)
  return {
    "name": "FRD",
    "path": str(final_path),
    "type": "markdown",
    "template": "frd.md.jinja"
  }
