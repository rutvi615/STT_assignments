#!/usr/bin/env python3
"""
Master script to run complete security analysis workflow.
This script orchestrates the entire vulnerability assessment process.
"""

import os
import subprocess
import sys

def check_tools():
    """Check if required security tools are installed."""
    tools = {
        'bandit': ['bandit', '--version'],
        'semgrep': ['semgrep', '--version'],
        'safety': ['safety', '--version'],
        'codeql': [r'D:/setup/codeql/codeql.exe', 'version']
    }
    
    missing_tools = []
    for tool, cmd in tools.items():
        try:
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=10)
            if result.returncode == 0:
                print(f"✓ {tool} is available")
            else:
                print(f"✗ {tool} check failed")
                missing_tools.append(tool)
        except (subprocess.TimeoutExpired, FileNotFoundError, subprocess.SubprocessError):
            print(f"✗ {tool} is not available")
            missing_tools.append(tool)
    
    if missing_tools:
        print(f"\nError: Missing tools: {', '.join(missing_tools)}")
        print("Please install the missing tools before running the analysis.")
        return False
    return True

def run_script(script_name, description):
    """Run a Python script and handle errors."""
    print(f"\n{'='*60}")
    print(f"STEP: {description}")
    print(f"Running: {script_name}")
    print(f"{'='*60}")
    
    try:
        result = subprocess.run([sys.executable, script_name], 
                              capture_output=True, text=True, timeout=300)
        
        if result.stdout:
            print("STDOUT:")
            print(result.stdout)
        
        if result.stderr:
            print("STDERR:")
            print(result.stderr)
        
        if result.returncode != 0:
            print(f"Warning: {script_name} completed with return code {result.returncode}")
        else:
            print(f"✓ {script_name} completed successfully")
            
        return result.returncode == 0
        
    except subprocess.TimeoutExpired:
        print(f"Error: {script_name} timed out")
        return False
    except Exception as e:
        print(f"Error running {script_name}: {e}")
        return False

def main():
    """Main orchestration function."""
    print("Security Analysis Workflow")
    print("="*50)
    
    # Check if we're in the right directory
    if not os.path.exists('main.py'):
        print("Error: Please run this script from the Lab6 directory")
        return 1
    
    # Check required tools
    print("Checking required tools...")
    if not check_tools():
        return 1
    
    # Step 1: Create CodeQL databases
    success = run_script('create_codeql_db.py', 
                        'Creating CodeQL databases for all projects')
    if not success:
        print("Warning: CodeQL database creation had issues, continuing...")
    
    # Step 2: Run all vulnerability scanners
    success = run_script('extract_findings.py', 
                        'Running all vulnerability scanners (Bandit, Semgrep, Safety, CodeQL)')
    if not success:
        print("Warning: Some vulnerability scanners had issues, continuing...")
    
    # Step 3: Consolidate results
    success = run_script('main.py', 
                        'Consolidating all findings into final report')
    if not success:
        print("Error: Failed to consolidate results")
        return 1
    
    # Final summary
    print(f"\n{'='*60}")
    print("ANALYSIS COMPLETE")
    print(f"{'='*60}")
    
    if os.path.exists('consolidated_findings.csv'):
        print("✓ Final report generated: consolidated_findings.csv")
        
        # Show summary statistics
        try:
            with open('consolidated_findings.csv', 'r', encoding='utf-8') as f:
                lines = f.readlines()
                if len(lines) > 1:  # More than just header
                    print(f"✓ Total findings: {len(lines) - 1} records")
                else:
                    print("ℹ No vulnerabilities found in any project")
        except Exception as e:
            print(f"Could not read summary: {e}")
    else:
        print("✗ No final report found")
        return 1
    
    print("\nResults are saved in:")
    print("- results/*/           : Individual tool outputs")
    print("- consolidated_findings.csv : Final consolidated report")
    
    return 0

if __name__ == "__main__":
    exit_code = main()
    sys.exit(exit_code)