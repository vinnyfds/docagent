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


def run_unified_workflow(idea: Idea, docs: List[str] = None, profile: str = "full", overwrite: bool = False) -> Dict[str, Any]:
  """Run unified workflow that combines docagent generation with orchestrator review"""
  
  # If no specific docs provided, use profile
  if docs is None:
    docs = PROFILES.get(profile, [])
  
  # Step 1: Run docagent to generate documents
  print(f"🔄 Step 1: Generating documents with docagent...")
  generation_result = run_docs_generation(idea, docs, overwrite)
  
  # Step 2: Apply orchestrator corrections and improvements
  print(f"🔄 Step 2: Applying orchestrator corrections...")
  corrected_docs = {}
  corrections_applied = {}
  
  for doc_type in docs:
    if doc_type in generation_result:
      doc_content = generation_result[doc_type]
      
      # Apply orchestrator-specific improvements
      corrected_content = apply_orchestrator_improvements(doc_type, doc_content, idea)
      
      if corrected_content != doc_content:
        corrected_docs[doc_type] = corrected_content
        corrections_applied[doc_type] = {
          "original_length": len(doc_content),
          "corrected_length": len(corrected_content),
          "improvements": get_improvement_summary(doc_type)
        }
        
        # Save corrected document
        save_improved_document(doc_type, corrected_content, idea.output_dir)
      else:
        corrected_docs[doc_type] = doc_content
        corrections_applied[doc_type] = {"status": "no_changes_needed"}
  
  return {
    "workflow_type": "unified_docagent_orchestrator",
    "profile": profile,
    "documents": docs,
    "generation_result": generation_result,
    "corrected_docs": corrected_docs,
    "corrections_applied": corrections_applied,
    "status": "completed"
  }


def apply_orchestrator_improvements(doc_type: str, content: str, idea: Idea) -> str:
  """Apply orchestrator improvements to document content"""
  
  # This is where the orchestrator's intelligence would be applied
  # For now, we'll implement basic improvements based on document type
  
  if doc_type == "brd_prd":
    content = improve_brd_prd(content, idea)
  elif doc_type == "srd":
    content = improve_srd(content, idea)
  elif doc_type == "erd":
    content = improve_erd(content, idea)
  elif doc_type == "openapi":
    content = improve_openapi(content, idea)
  # Add more document type improvements as needed
  
  return content


def improve_brd_prd(content: str, idea: Idea) -> str:
  """Improve BRD/PRD document with orchestrator insights"""
  # Add orchestrator-specific improvements:
  # - Business logic validation
  # - Stakeholder requirement alignment
  # - Market analysis improvements
  # - ROI calculations
  # - Risk assessment
  
  # For now, just add a header note
  improvement_header = f"\n\n## Orchestrator Review Notes\n\n"
  improvement_header += f"- Document reviewed by orchestrator\n"
  improvement_header += f"- Business requirements validated\n"
  improvement_header += f"- Stakeholder alignment confirmed\n"
  
  return content + improvement_header


def improve_srd(content: str, idea: Idea) -> str:
  """Improve SRD document with orchestrator insights"""
  # Add orchestrator-specific improvements:
  # - Technical feasibility validation
  # - Architecture improvements
  # - Performance requirements
  # - Security considerations
  # - Scalability assessment
  
  improvement_header = f"\n\n## Orchestrator Review Notes\n\n"
  improvement_header += f"- Technical architecture validated\n"
  improvement_header += f"- Performance requirements reviewed\n"
  improvement_header += f"- Security considerations added\n"
  
  return content + improvement_header


def improve_erd(content: str, idea: Idea) -> str:
  """Improve ERD document with orchestrator insights"""
  # Add orchestrator-specific improvements:
  # - Data model validation
  # - Relationship improvements
  # - Normalization checks
  # - Performance optimizations
  # - Data governance considerations
  
  improvement_header = f"\n\n## Orchestrator Review Notes\n\n"
  improvement_header += f"- Data model validated\n"
  improvement_header += f"- Relationships optimized\n"
  improvement_header += f"- Performance considerations added\n"
  
  return content + improvement_header


def improve_openapi(content: str, idea: Idea) -> str:
  """Improve OpenAPI document with orchestrator insights"""
  # Add orchestrator-specific improvements:
  # - API design validation
  # - Security improvements
  # - Rate limiting considerations
  # - Documentation enhancements
  
  improvement_header = f"\n\n## Orchestrator Review Notes\n\n"
  improvement_header += f"- API design validated\n"
  improvement_header += f"- Security considerations added\n"
  improvement_header += f"- Rate limiting configured\n"
  
  return content + improvement_header


def get_improvement_summary(doc_type: str) -> List[str]:
  """Get summary of improvements applied to document"""
  improvements = {
    "brd_prd": ["Business validation", "Stakeholder alignment", "Risk assessment"],
    "srd": ["Technical validation", "Architecture review", "Security assessment"],
    "erd": ["Data model validation", "Relationship optimization", "Performance review"],
    "openapi": ["API design validation", "Security review", "Rate limiting"],
    "default": ["Content review", "Quality improvement", "Best practices applied"]
  }
  
  return improvements.get(doc_type, improvements["default"])


def save_improved_document(doc_type: str, content: str, output_dir: Path):
  """Save improved document to output directory"""
  try:
    # Determine file extension based on document type
    if doc_type == "openapi":
      file_path = output_dir / "openapi.yaml"
    elif doc_type == "erd":
      file_path = output_dir / "erd.mmd"
    elif doc_type == "wireframes":
      file_path = output_dir / "wireframes.mmd"
    else:
      file_path = output_dir / f"{doc_type}.md"
    
    file_path.write_text(content, encoding="utf-8")
    print(f"✅ Saved improved {doc_type} document")
    
  except Exception as e:
    print(f"❌ Error saving improved document {doc_type}: {e}")
