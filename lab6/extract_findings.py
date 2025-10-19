import os
import subprocess

def run_bandit(repo_path, output_path):
    cmd = [
        "bandit", "-r", repo_path, "-f", "json", "-o", output_path
    ]
    subprocess.run(cmd, check=False)

def run_semgrep(repo_path, output_path):
    cmd = [
        "semgrep", "--config=auto", repo_path, "--json", "--output", output_path
    ]
    subprocess.run(cmd, check=False)

def run_safety(repo_path, output_path):
    # Safety checks dependencies, so we look for requirements files
    req_files = []
    for root, dirs, files in os.walk(repo_path):
        for file in files:
            if file in ['requirements.txt', 'requirements-dev.txt', 'Pipfile']:
                req_files.append(os.path.join(root, file))
    
    if not req_files:
        print(f"No requirements files found for {repo_path}")
        # Create empty JSON structure
        with open(output_path, "w", encoding="utf-8") as f:
            import json
            json.dump({"vulnerabilities": []}, f)
        return
    
    # Use the first requirements file found
    req_file = req_files[0]
    cmd = ["safety", "check", "-r", req_file, "--json", "--output", output_path]
    result = subprocess.run(cmd, capture_output=True, text=True)
    
    # Safety returns non-zero exit code when vulnerabilities are found
    # So we need to write the output manually if it failed
    if result.returncode != 0 and result.stdout:
        with open(output_path, "w", encoding="utf-8") as f:
            f.write(result.stdout)
    elif not os.path.exists(output_path):
        # Create empty JSON if no output was generated
        with open(output_path, "w", encoding="utf-8") as f:
            import json
            json.dump({"vulnerabilities": []}, f)

def run_codeql(repo_path, output_path, db_path):
    import csv
    import json
    
    codeql_path = r"D:/setup/codeql/codeql.exe"  # Use your actual path
    csv_output = output_path.replace('.json', '.csv')
    
    subprocess.run([
        codeql_path, "database", "analyze", db_path,
        "codeql/python-queries",
        "--format=csv", "--output", csv_output
    ], check=False)

    # Mapping dictionary: query name to CWE ID
    codeql_to_cwe = {
        "Clear-text logging of sensitive information": "CWE-532",
        "Use of a broken or risky cryptographic algorithm": "CWE-327",
        "Use of hard-coded password": "CWE-259",
        "Missing authentication for critical function": "CWE-306",
        "Incomplete regular expression for hostnames": "CWE-20",
        "SQL query built from user-controlled sources": "CWE-89",
        "Code injection": "CWE-94",
        "Hard-coded credentials": "CWE-798",
        "Uncontrolled data used in path expression": "CWE-22",
        "Weak cryptographic algorithm": "CWE-327",
        "Information exposure through an error message": "CWE-209",
        "Use of externally-controlled input to select classes or code": "CWE-470",
        "Deserialization of untrusted data": "CWE-502",
        "Missing rate limiting": "CWE-770",
        "Unsafe shell command constructed from library input": "CWE-78",
        # Add more mappings as needed
    }

    # Convert CSV to JSON format
    results = {"results": []}
    
    if os.path.exists(csv_output) and os.path.getsize(csv_output) > 0:
        try:
            with open(csv_output, "r", encoding="utf-8") as f:
                reader = csv.reader(f)
                # CodeQL CSV doesn't have headers, format is:
                # query_name, description, severity, message, file_path, start_line, start_col, end_line, end_col
                for row in reader:
                    if row and len(row) >= 5:  # Ensure we have enough columns
                        query_name = row[0].strip('"')
                        cwe_id = codeql_to_cwe.get(query_name, "")
                        if cwe_id:  # Only include findings with CWE mapping
                            result = {
                                "query": query_name,
                                "file": row[4],  # file_path is at index 4
                                "line": row[5] if len(row) > 5 else "N/A",   # start_line
                                "column": row[6] if len(row) > 6 else "N/A", # start_col
                                "message": row[3],  # message is at index 3
                                "cwe_id": cwe_id
                            }
                            results["results"].append(result)
                        else:
                            # Include all findings, even without CWE mapping for debugging
                            result = {
                                "query": query_name,
                                "file": row[4] if len(row) > 4 else "N/A",
                                "line": row[5] if len(row) > 5 else "N/A",
                                "column": row[6] if len(row) > 6 else "N/A",
                                "message": row[3] if len(row) > 3 else "N/A",
                                "cwe_id": ""  # No CWE mapping available
                            }
                            results["results"].append(result)
        except Exception as e:
            print(f"Error processing CodeQL results: {e}")
    else:
        print(f"CodeQL analysis produced no results for {repo_path}")
    
    # Write JSON output
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(results, f, indent=2)

def main():
    repos = ["chalice", "gpt-researcher", "pythonrobotics"]
    results_dir = "results"
    os.makedirs(results_dir, exist_ok=True)

    for project in repos:
        repo_path = os.path.join(project)
        if not os.path.isdir(repo_path):
            print(f"{repo_path} is not a directory, skipping.")
            continue
        project_results = os.path.join(results_dir, project)
        os.makedirs(project_results, exist_ok=True)

        print(f"Running Bandit on {project}...")
        run_bandit(repo_path, os.path.join(project_results, "bandit.json"))
        print()

        print(f"Running Semgrep on {project}...")
        run_semgrep(repo_path, os.path.join(project_results, "semgrep.json"))
        print()

        print(f"Running Safety on {project}...")
        run_safety(repo_path, os.path.join(project_results, "safety.json"))
        print()

        print(f"Running CodeQL on {project}...")
        db_path = os.path.join(project_results, "codeql-db")
        run_codeql(repo_path, os.path.join(project_results, "codeql.json"), db_path)
        print()

if __name__ == "__main__":
    main()
