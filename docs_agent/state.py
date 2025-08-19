"""State models for DocGen Suite"""

from typing import List, Dict, Optional, Any
from pathlib import Path
from pydantic import BaseModel, Field
from datetime import datetime


class Context(BaseModel):
  """Context information for document generation"""
  project_name: str = Field(..., description="Project name")
  domain: str = Field(..., description="Business domain")
  stakeholders: List[str] = Field(default_factory=list, description="Key stakeholders")
  constraints: List[str] = Field(default_factory=list, description="Project constraints")
  assumptions: List[str] = Field(default_factory=list, description="Key assumptions")


class Idea(BaseModel):
  """Core idea specification for document generation"""
  title: str = Field(..., description="Project title")
  description: str = Field(..., description="Project description")
  context: Context = Field(..., description="Project context")
  personas: List[str] = Field(default_factory=list, description="Target user personas")
  kpis: List[str] = Field(default_factory=list, description="Key performance indicators")
  modules: List[str] = Field(default_factory=list, description="System modules")
  entities: List[str] = Field(default_factory=list, description="Data entities")
  apis: List[str] = Field(default_factory=list, description="API endpoints")
  compliance: List[str] = Field(default_factory=list, description="Compliance requirements")
  slas: Dict[str, str] = Field(default_factory=dict, description="Service level agreements")
  created_at: datetime = Field(default_factory=datetime.now)
  version: str = Field(default="1.0.0", description="Idea version")
  
  # Workflow fields
  docs: Optional[List[str]] = Field(default_factory=list, description="Document types to generate")
  overwrite: Optional[bool] = Field(default=False, description="Allow overwriting existing files")
  output_dir: Path = Field(default=Path("docs_agent/outputs"), description="Directory to write artifacts")


class DocRequest(BaseModel):
  """Request for specific document generation"""
  idea: Idea = Field(..., description="Idea to generate docs for")
  docs: List[str] = Field(default_factory=list, description="Document types to generate")
  overwrite: bool = Field(default=False, description="Allow overwriting existing files")
  output_dir: Path = Field(default=Path("docs_agent/outputs"), description="Output directory")


class DocArtifacts(BaseModel):
  """Generated document artifacts"""
  idea_hash: str = Field(..., description="Hash of the input idea")
  generated_at: datetime = Field(default_factory=datetime.now)
  artifacts: List[Dict[str, Any]] = Field(default_factory=list, description="Generated artifacts")
  
  # Document paths
  brd_prd: Optional[Path] = Field(None, description="BRD/PRD document path")
  frd: Optional[Path] = Field(None, description="FRD document path")
  srd: Optional[Path] = Field(None, description="SRD document path")
  trd_tdd: Optional[Path] = Field(None, description="TRD/TDD document path")
  erd: Optional[Path] = Field(None, description="ERD document path")
  openapi: Optional[Path] = Field(None, description="OpenAPI specification path")
  wireframes: Optional[Path] = Field(None, description="Wireframes document path")
  design_system: Optional[Path] = Field(None, description="Design system document path")
  project_plan: Optional[Path] = Field(None, description="Project plan document path")
  test_strategy: Optional[Path] = Field(None, description="Test strategy document path")
  cicd_env: Optional[Path] = Field(None, description="CI/CD environment document path")
  release_runbook: Optional[Path] = Field(None, description="Release runbook document path")
