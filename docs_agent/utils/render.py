"""Template rendering utilities for DocGen Suite"""

from pathlib import Path
from typing import Any, Dict
from jinja2 import Environment, FileSystemLoader, StrictUndefined


def render_template(template_name: str, data: Dict[str, Any]) -> str:
  """Render a Jinja2 template with strict undefined handling"""
  # Get the templates directory
  templates_dir = Path(__file__).parent.parent / "prompts"
  
  # Create Jinja2 environment with strict undefined
  env = Environment(
    loader=FileSystemLoader(str(templates_dir)),
    undefined=StrictUndefined,
    trim_blocks=True,
    lstrip_blocks=True
  )
  
  # Load and render template
  template = env.get_template(template_name)
  return template.render(**data)


def render_template_from_string(template_string: str, data: Dict[str, Any]) -> str:
  """Render a Jinja2 template from string content"""
  env = Environment(
    undefined=StrictUndefined,
    trim_blocks=True,
    lstrip_blocks=True
  )
  
  template = env.from_string(template_string)
  return template.render(**data)
