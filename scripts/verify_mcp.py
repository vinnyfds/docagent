#!/usr/bin/env python3
"""Verify core components are working"""

import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent))

from docs_agent.state import Idea


def create_sample_idea():
  """Create a sample idea for testing"""
  return Idea(
    title="Sample SaaS Platform",
    description="A comprehensive SaaS platform for business management",
    context={
      "project_name": "BusinessManager SaaS",
      "domain": "Business Management",
      "stakeholders": ["CTO", "Product Manager", "Development Team"],
      "constraints": ["Budget: $500K", "Timeline: 6 months"],
      "assumptions": ["Cloud-first approach", "Modern tech stack"]
    },
    personas=["Business Owner", "Manager", "Employee"],
    kpis=["User adoption rate", "Feature usage", "Customer satisfaction"],
    modules=["User Management", "Project Management", "Analytics"],
    entities=["User", "Project", "Task", "Report"],
    apis=["User API", "Project API", "Analytics API"],
    compliance=["GDPR", "SOC 2"],
    slas={"Uptime": "99.9%", "Response Time": "<200ms"}
  )


def test_state_models():
  """Test Pydantic state models"""
  print("Testing state models...")
  
  try:
    idea = create_sample_idea()
    print("✓ Idea model created successfully")
    
    # Test JSON serialization
    idea_json = idea.model_dump_json()
    print("✓ JSON serialization successful")
    
    # Test JSON deserialization
    idea_from_json = Idea.model_validate_json(idea_json)
    print("✓ JSON deserialization successful")
    
    return True
  except Exception as e:
    print(f"✗ State model test failed: {e}")
    return False


def test_template_rendering():
  """Test template rendering"""
  print("Testing template rendering...")
  
  try:
    from docs_agent.utils.render import render_template
    
    idea = create_sample_idea()
    content = render_template("brd_prd.md.jinja", {"idea": idea})
    
    if content and len(content) > 100:
      print("✓ Template rendering successful")
      return True
    else:
      print("✗ Template rendering failed: content too short")
      return False
  except Exception as e:
    print(f"✗ Template rendering test failed: {e}")
    return False


def test_safe_write():
  """Test safe file writing"""
  print("Testing safe file writing...")
  
  try:
    from docs_agent.utils.safety import safe_write
    
    test_dir = Path("test_output")
    test_dir.mkdir(exist_ok=True)
    
    test_file = test_dir / "test.txt"
    content = "Test content"
    
    # Test safe write
    final_path = safe_write(test_file, content, overwrite=False)
    print("✓ Safe write successful")
    
    # Test .new suffix when file exists
    if test_file.exists():
      new_path = safe_write(test_file, "New content", overwrite=False)
      if ".new" in str(new_path):
        print("✓ .new suffix handling successful")
      else:
        print("✗ .new suffix handling failed")
    
    # Cleanup
    import shutil
    shutil.rmtree(test_dir)
    
    return True
  except Exception as e:
    print(f"✗ Safe write test failed: {e}")
    return False


def main():
  """Run all verification tests"""
  print("DocGen Suite - MCP Verification")
  print("=" * 40)
  
  tests = [
    test_state_models,
    test_template_rendering,
    test_safe_write
  ]
  
  passed = 0
  total = len(tests)
  
  for test in tests:
    if test():
      passed += 1
    print()
  
  print(f"Results: {passed}/{total} tests passed")
  
  if passed == total:
    print("✓ All tests passed! MCP servers should work correctly.")
    return 0
  else:
    print("✗ Some tests failed. Please check the errors above.")
    return 1


if __name__ == "__main__":
  sys.exit(main())
