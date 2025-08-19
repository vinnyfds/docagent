"""ERD and API document generation node"""

from pathlib import Path
from typing import Dict, Any
from ..state import Idea
from ..utils.render import render_template
from ..utils.safety import safe_write


def generate_erd_api(state: Idea) -> Dict[str, Any]:
  """Generate ERD and API documents"""
  artifacts = []
  dest_dir = state.output_dir
  overwrite = state.overwrite or False
  
  erd_content = render_template("erd.mmd.jinja", {"idea": state})
  erd_path = dest_dir / "erd.mmd"
  final_erd_path = safe_write(erd_path, erd_content, overwrite)
  artifacts.append({
    "name": "ERD",
    "path": str(final_erd_path),
    "type": "mermaid",
    "template": "erd.mmd.jinja"
  })
  
  openapi_content = render_template("openapi.yaml.jinja", {"idea": state})
  openapi_path = dest_dir / "openapi.yaml"
  final_openapi_path = safe_write(openapi_path, openapi_content, overwrite)
  artifacts.append({
    "name": "OpenAPI",
    "path": str(final_openapi_path),
    "type": "yaml",
    "template": "openapi.yaml.jinja"
  })
  
  return {
    "name": "ERD and API",
    "artifacts": artifacts,
    "type": "multiple",
    "templates": ["erd.mmd.jinja", "openapi.yaml.jinja"]
  }
