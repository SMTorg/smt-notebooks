#!/usr/bin/env python3
"""
Script to execute all Jupyter notebooks in the repository.
Exits with non-zero status if any notebook fails to execute.
"""

import os
import sys
import glob
import argparse
import warnings
import nbformat
from nbconvert.preprocessors import ExecutePreprocessor
from nbconvert.preprocessors.execute import CellExecutionError

# Suppress common warnings during execution
warnings.filterwarnings('ignore', category=RuntimeWarning, module='zmq')
warnings.filterwarnings('ignore', category=UserWarning, module='sklearn')

def execute_notebook(notebook_path):
    """
    Execute a single notebook and return True if successful, False otherwise.
    """
    print(f"Executing: {notebook_path}")
    
    try:
        # Read the notebook
        with open(notebook_path, 'r', encoding='utf-8') as f:
            nb = nbformat.read(f, as_version=4)
        
        # Create an executor with a timeout (10 minutes per notebook)
        ep = ExecutePreprocessor(timeout=600, kernel_name='python3')
        
        # Execute the notebook
        ep.preprocess(nb, {'metadata': {'path': os.path.dirname(notebook_path)}})
        
        # Save the executed notebook with outputs
        with open(notebook_path, 'w', encoding='utf-8') as f:
            nbformat.write(nb, f)
        
        print(f"✓ Successfully executed: {notebook_path}")
        return True
        
    except CellExecutionError as e:
        print(f"✗ Cell execution failed in {notebook_path}:")
        print(f"  Error: {str(e).split(chr(10))[0]}")
        return False
    except Exception as e:
        print(f"✗ Failed to execute {notebook_path}:")
        print(f"  Error: {str(e).split(chr(10))[0]}")
        return False

def main():
    """
    Find and execute all notebooks in the repository.
    """
    # Parse command-line arguments
    parser = argparse.ArgumentParser(
        description='Execute Jupyter notebooks.'
    )
    parser.add_argument(
        '-d', '--directory',
        type=str,
        default=None,
        help='Directory to search for notebooks recursively (default: None)'
    )
    parser.add_argument(
        '-f', '--file',
        type=str,
        default=None,
        help='Specific notebook file to execute (default: None)'
    )
    args = parser.parse_args()
    
    # Validate arguments: either -d or -f must be provided, but not both
    if args.directory is not None and args.file is not None:
        print("Error: Cannot specify both -d and -f options. Please use one or the other.")
        sys.exit(1)
    
    if args.directory is None and args.file is None:
        # Default behavior: search current directory
        args.directory = '.'
    
    # Find notebooks based on the provided arguments
    if args.file:
        # Execute a single specific notebook
        if not os.path.isfile(args.file):
            print(f"Error: Notebook file '{args.file}' not found.")
            sys.exit(1)
        notebooks = [args.file]
    else:
        # Find all .ipynb files in the specified directory
        search_pattern = os.path.join(args.directory, '**', '*.ipynb')
        notebooks = glob.glob(search_pattern, recursive=True)
        
        # Filter out any notebooks in hidden directories or node_modules
        notebooks = [nb for nb in notebooks if not any(part.startswith('.') or part == 'node_modules' 
                                                        for part in nb.split(os.sep))]
        
        if not notebooks:
            print(f"No notebooks found in '{args.directory}'")
            sys.exit(0)
    
    print(f"Found {len(notebooks)} notebook(s) to execute:")
    for nb in notebooks:
        print(f"  - {nb}")
    print()
    
    # Execute all notebooks
    results = []
    for notebook_path in notebooks:
        success = execute_notebook(notebook_path)
        results.append((notebook_path, success))
        print()
    
    # Print summary
    print("=" * 60)
    print("SUMMARY")
    print("=" * 60)
    
    passed = sum(1 for _, success in results if success)
    failed = sum(1 for _, success in results if not success)
    
    print(f"Total notebooks: {len(notebooks)}")
    print(f"Passed: {passed}")
    print(f"Failed: {failed}")
    
    if failed > 0:
        print("\nFailed notebooks:")
        for nb, success in results:
            if not success:
                print(f"  - {nb}")
        sys.exit(1)
    else:
        print("\nAll notebooks executed successfully!")
        sys.exit(0)

if __name__ == "__main__":
    main()
