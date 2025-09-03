#!/usr/bin/env python3
"""
Master Orchestrator Script - Executes all repository analysis modules
"""

import subprocess
import sys
import os

def execute_module(file_name):
    """Execute a Python module and handle results"""
    print(f"\n{'-'*55}")
    print(f"Executing module: {file_name}")
    print(f"{'-'*55}")
    
    try:
        process = subprocess.run([sys.executable, file_name],
                                 capture_output=True, text=True)
        
        if process.returncode == 0:
            print(f"SUCCESS: {file_name} finished")
            if process.stdout.strip():
                print(process.stdout)
        else:
            print(f"FAILURE: {file_name} did not finish correctly")
            if process.stderr.strip():
                print(process.stderr)
            return False

    except Exception as err:
        print(f"⚠ Runtime Exception: {str(err)}")
        return False
    
    return True


def main():
    print("===== Repository Workflow Automation =====")
    
    # Verify Python packages
    try:
        import numpy, pandas, matplotlib
        print("✔ Dependencies located")
    except ImportError as missing:
        print(f"Missing package: {missing}")
        print("Try installing with: pip install numpy pandas matplotlib")
        return
    
    # Prepare output directories
    os.makedirs('../01_CSV_Datasets', exist_ok=True)
    os.makedirs('../03_Generated_Graphs', exist_ok=True)
    
    # Define execution order
    pipeline = [
        "01_generate_csv_datasets.py",
        "02_generate_individual_graphs.py", 
        "03_generate_statistics.py"
    

    ]
    
    completed = 0
    for module in pipeline:
        if execute_module(module):
            completed += 1
        else:
            break
    
    # Final report
    print(f"\n{'='*60}")
    if completed == len(pipeline):
        print("Workflow finished successfully!")
        print("\nOutput summary:")
        print(" ../01_CSV_Datasets/  → generated CSV datasets")
        print("../03_Generated_Graphs/ → created visual graphs")
    else:
        print(f"{len(pipeline) - completed} module(s) failed")


if __name__ == "__main__":
    main()
