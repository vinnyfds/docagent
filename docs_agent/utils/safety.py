"""Safe file writing utilities for DocGen Suite"""

import hashlib
from pathlib import Path
from typing import Optional


def safe_write(path: Path, text: str, overwrite: bool = False) -> Path:
  """Safely write text to file with collision handling"""
  # Ensure parent directory exists
  path.parent.mkdir(parents=True, exist_ok=True)
  
  # If file exists and overwrite is False, use .new suffix
  if path.exists() and not overwrite:
    new_path = path.with_suffix(path.suffix + ".new")
    path = new_path
  
  # Write content
  path.write_text(text, encoding="utf-8")
  return path


def get_file_hash(path: Path) -> str:
  """Get SHA256 hash of file content"""
  if not path.exists():
    return ""
  
  content = path.read_bytes()
  return hashlib.sha256(content).hexdigest()[:16]


def safe_append(path: Path, text: str) -> Path:
  """Safely append text to existing file"""
  # Ensure parent directory exists
  path.parent.mkdir(parents=True, exist_ok=True)
  
  # Append content
  with path.open("a", encoding="utf-8") as f:
    f.write(text)
  
  return path


def backup_file(path: Path, suffix: str = ".backup") -> Optional[Path]:
  """Create backup of existing file"""
  if not path.exists():
    return None
  
  backup_path = path.with_suffix(path.suffix + suffix)
  backup_path.write_bytes(path.read_bytes())
  return backup_path
