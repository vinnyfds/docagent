#!/usr/bin/env python3
"""CLI script for DocGen Suite"""

import argparse
import json
import sys
from pathlib import Path

# Add parent directory to Python path
sys.path.insert(0, str(Path(__file__).parent.parent))

from docs_agent.state import Idea, Context


def main():
  parser = argparse.ArgumentParser(description="Generate documents using DocGen Suite")
  parser.add_argument("--idea", required=True, help="Path to idea JSON file")
  parser.add_argument("--docs", help="Comma-separated list of document types")
  parser.add_argument("--all", action="store_true", help="Generate all documents")
  parser.add_argument("--overwrite", action="store_true", help="Allow overwriting existing files")
  
  args = parser.parse_args()
  
  try:
    # Load idea from JSON
    with open(args.idea, 'r') as f:
      idea_data = json.load(f)
    
    print(f"Loaded JSON data: {idea_data.keys()}")
    
    # Create Context object from nested data
    if 'context' in idea_data:
      context_data = idea_data.pop('context')
      print(f"Context data: {context_data}")
      idea_data['context'] = Context(**context_data)
      print(f"Context object created: {idea_data['context']}")
    
    print(f"Final idea data keys: {idea_data.keys()}")
    
    idea = Idea(**idea_data)
    print(f"Idea object created successfully: {idea.title}")
    
    if args.all:
      # Generate all documents
      from docs_agent.graph import generate_all_documents
      result = generate_all_documents(idea, args.overwrite)
      print("Generated all documents successfully")
    elif args.docs:
      # Generate specific documents
      from docs_agent.graph import run_docs_generation
      docs = [doc.strip() for doc in args.docs.split(",")]
      result = run_docs_generation(idea, docs, args.overwrite)
      print(f"Generated documents: {', '.join(docs)}")
    else:
      print("Error: Must specify --docs or --all")
      sys.exit(1)
    
    print(f"Output directory: {Path('outputs')}")
    
  except Exception as e:
    print(f"Error: {e}")
    import traceback
    traceback.print_exc()
    sys.exit(1)


if __name__ == "__main__":
  main()
