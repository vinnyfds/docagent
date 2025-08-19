"""SRD document generation node"""

from pathlib import Path
from typing import Dict, Any
from ..state import Idea
from ..utils.render import render_template
from ..utils.safety import safe_write


def generate_srd(state: Idea) -> Dict[str, Any]:
  """Generate SRD document"""
  content = render_template("srd.md.jinja", {"idea": state})
  dest_dir = state.output_dir
  output_path = dest_dir / "srd.md"
  final_path = safe_write(output_path, content, state.overwrite or False)
  return {
    "name": "SRD",
    "path": str(final_path),
    "type": "markdown",
    "template": "srd.md.jinja"
  }
