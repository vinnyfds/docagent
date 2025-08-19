"""Orchestrator graph for DocGen Suite"""

from typing import Dict, Any, List
from pathlib import Path
from langgraph.graph import StateGraph, END
from docs_agent.state import Idea, DocRequest
from docs_agent.graph import run_docs_generation


# Profile definitions
PROFILES = {
  "full": [
    "brd_prd", "frd", "srd", "trd_tdd", "erd", "openapi",
    "wireframes", "design_system", "project_plan", "test_strategy", 
    "cicd_env", "release_runbook"
  ],
  "lean": [
    "brd_prd", "srd", "erd", "project_plan", "test_strategy"
  ],
  "tech_only": [
    "srd", "trd_tdd", "erd", "openapi", "cicd_env"
  ],
  "pm_only": [
    "brd_prd", "frd", "project_plan", "test_strategy", "release_runbook"
  ]
}


def create_orchestrator_graph():
  """Create orchestrator workflow graph"""
  
  workflow = StateGraph(DocRequest)
  
  # Add orchestration node
  workflow.add_node("orchestrate", lambda state: state)
  
  # Set entry point
  workflow.set_entry_point("orchestrate")
  
  # Add edge to end
  workflow.add_edge("orchestrate", END)
  
  return workflow


def orchestrate_docgen(idea: Idea, profile: str = "full", overwrite: bool = False) -> Dict[str, Any]:
  """Orchestrate document generation based on profile"""
  
  # Get document list for profile
  if profile not in PROFILES:
    raise ValueError(f"Unknown profile: {profile}. Available: {list(PROFILES.keys())}")
  
  docs = PROFILES[profile]
  
  # Run document generation
  result = run_docs_generation(idea, docs, overwrite)
  
  return {
    "profile": profile,
    "documents": docs,
    "result": result
  }
