"""LangGraph for DocGen Suite"""

from typing import Dict, Any, List
from pathlib import Path
from langgraph.graph import StateGraph, END
from .state import Idea, DocRequest, DocArtifacts
from .nodes import (
  generate_brd_prd,
  generate_frd,
  generate_srd,
  generate_trd_tdd,
  generate_erd_api,
  generate_ui_wireframes,
  generate_project_plan,
  generate_test_strategy,
  generate_cicd_env,
  generate_release_runbook
)


def create_docs_graph() -> StateGraph:
  """Create the document generation graph"""
  
  # Create the graph with Idea as state
  workflow = StateGraph(Idea)
  
  # Add nodes
  workflow.add_node("generate_brd_prd", generate_brd_prd)
  workflow.add_node("generate_frd", generate_frd)
  workflow.add_node("generate_srd", generate_srd)
  workflow.add_node("generate_trd_tdd", generate_trd_tdd)
  workflow.add_node("generate_erd_api", generate_erd_api)
  workflow.add_node("generate_ui_wireframes", generate_ui_wireframes)
  workflow.add_node("generate_project_plan", generate_project_plan)
  workflow.add_node("generate_test_strategy", generate_test_strategy)
  workflow.add_node("generate_cicd_env", generate_cicd_env)
  workflow.add_node("generate_release_runbook", generate_release_runbook)
  
  # Define the workflow
  workflow.set_entry_point("generate_brd_prd")
  
  # Add conditional edges based on requested documents
  workflow.add_conditional_edges(
    "generate_brd_prd",
    lambda state: "generate_frd" if "frd" in getattr(state, 'docs', []) else "generate_srd"
  )
  
  workflow.add_conditional_edges(
    "generate_frd",
    lambda state: "generate_srd" if "srd" in getattr(state, 'docs', []) else "generate_trd_tdd"
  )
  
  workflow.add_conditional_edges(
    "generate_srd",
    lambda state: "generate_trd_tdd" if "trd_tdd" in getattr(state, 'docs', []) else "generate_erd_api"
  )
  
  workflow.add_conditional_edges(
    "generate_trd_tdd",
    lambda state: "generate_erd_api" if "erd" in getattr(state, 'docs', []) or "openapi" in getattr(state, 'docs', []) else "generate_ui_wireframes"
  )
  
  workflow.add_conditional_edges(
    "generate_erd_api",
    lambda state: "generate_ui_wireframes" if "wireframes" in getattr(state, 'docs', []) else "generate_project_plan"
  )
  
  workflow.add_conditional_edges(
    "generate_ui_wireframes",
    lambda state: "generate_project_plan" if "project_plan" in getattr(state, 'docs', []) else "generate_test_strategy"
  )
  
  workflow.add_conditional_edges(
    "generate_project_plan",
    lambda state: "generate_test_strategy" if "test_strategy" in getattr(state, 'docs', []) else "generate_cicd_env"
  )
  
  workflow.add_conditional_edges(
    "generate_test_strategy",
    lambda state: "generate_cicd_env" if "cicd_env" in getattr(state, 'docs', []) else "generate_release_runbook"
  )
  
  workflow.add_conditional_edges(
    "generate_cicd_env",
    lambda state: "generate_release_runbook" if "release_runbook" in getattr(state, 'docs', []) else END
  )
  
  workflow.add_edge("generate_release_runbook", END)
  
  return workflow


def run_docs_generation(idea: Idea, docs: List[str], overwrite: bool = False) -> Dict[str, Any]:
  """Run document generation workflow"""
  
  # Add docs to idea for conditional logic
  idea.docs = docs
  idea.overwrite = overwrite
  
  # Create and run graph
  graph = create_docs_graph()
  app = graph.compile()
  
  # Execute workflow
  result = app.invoke(idea)
  
  return result


def generate_all_documents(idea: Idea, overwrite: bool = False) -> Dict[str, Any]:
  """Generate all document types"""
  
  all_docs = [
    "brd_prd", "frd", "srd", "trd_tdd", "erd", "openapi",
    "wireframes", "project_plan", "test_strategy", "cicd_env", "release_runbook"
  ]
  
  return run_docs_generation(idea, all_docs, overwrite)
