import os
import json
import csv

TOP_25_CWE = {
    "CWE-79", "CWE-89", "CWE-787", "CWE-20", "CWE-125", "CWE-78", "CWE-416",
    "CWE-22", "CWE-352", "CWE-434", "CWE-190", "CWE-476", "CWE-502", "CWE-306",
    "CWE-798", "CWE-862", "CWE-276", "CWE-94", "CWE-611", "CWE-863",
    "CWE-732", "CWE-829", "CWE-327", "CWE-200",
    # Support both formats (with and without CWE- prefix)
    "78", "89", "787", "20", "125", "416",
    "22", "352", "434", "190", "476", "502", "306",
    "798", "862", "276", "94", "611", "863",
    "732", "829", "327", "200"
}

def parse_bandit(json_path):
    try:
        with open(json_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
    except UnicodeDecodeError:
        with open(json_path, 'r', encoding='utf-8', errors='ignore') as f:
            data = json.load(f)
    findings = {}
    for item in data.get("results", []):
        cwe = item.get("issue_cwe", [])
        if isinstance(cwe, list):
            for cwe_id in cwe:
                if isinstance(cwe_id, str):
                    findings[cwe_id] = findings.get(cwe_id, 0) + 1
                elif isinstance(cwe_id, dict) and "id" in cwe_id:
                    cwe_str = cwe_id["id"]
                    findings[cwe_str] = findings.get(cwe_str, 0) + 1
        elif isinstance(cwe, str):
            findings[cwe] = findings.get(cwe, 0) + 1
        elif isinstance(cwe, dict) and "id" in cwe:
            cwe_str = cwe["id"]
            findings[cwe_str] = findings.get(cwe_str, 0) + 1
    return findings

def parse_semgrep(json_path):
    try:
        with open(json_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
    except UnicodeDecodeError:
        # Try with different encoding
        with open(json_path, 'r', encoding='utf-8', errors='ignore') as f:
            data = json.load(f)
    findings = {}
    for item in data.get("results", []):
        cwe_data = item.get("extra", {}).get("metadata", {}).get("cwe")
        if cwe_data:
            if isinstance(cwe_data, list):
                for cwe_item in cwe_data:
                    if isinstance(cwe_item, str):
                        # Extract CWE-XXX from strings like "CWE-22: Improper Limitation..."
                        if cwe_item.startswith("CWE-"):
                            cwe_id = cwe_item.split(":")[0].strip()
                            findings[cwe_id] = findings.get(cwe_id, 0) + 1
            elif isinstance(cwe_data, str):
                # Extract CWE-XXX from strings like "CWE-22: Improper Limitation..."
                if cwe_data.startswith("CWE-"):
                    cwe_id = cwe_data.split(":")[0].strip()
                    findings[cwe_id] = findings.get(cwe_id, 0) + 1
    return findings

def parse_safety(json_path):
    try:
        with open(json_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
    except UnicodeDecodeError:
        with open(json_path, 'r', encoding='utf-8', errors='ignore') as f:
            data = json.load(f)
    findings = {}
    for vuln in data.get("vulnerabilities", []):
        cwe_id = vuln.get("cwe")
        if cwe_id:
            findings[cwe_id] = findings.get(cwe_id, 0) + 1
    return findings

def parse_codeql(json_path):
    try:
        with open(json_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
    except UnicodeDecodeError:
        with open(json_path, 'r', encoding='utf-8', errors='ignore') as f:
            data = json.load(f)
    findings = {}
    for item in data.get("results", []):
        cwe_id = item.get("cwe_id")
        if cwe_id and cwe_id.strip():  # Only count non-empty CWE IDs
            findings[cwe_id] = findings.get(cwe_id, 0) + 1
    return findings

def aggregate_findings(project_name, tool_name, findings):
    rows = []
    for cwe_id, count in findings.items():
        is_top_25 = "Yes" if cwe_id in TOP_25_CWE else "No"
        rows.append([project_name, tool_name, cwe_id, count, is_top_25])
    return rows

def main():
    results_dir = "results"
    output_csv = "consolidated_findings.csv"
    all_rows = []

    for project in os.listdir(results_dir):
        project_path = os.path.join(results_dir, project)
        if not os.path.isdir(project_path):
            continue
        for tool_file in os.listdir(project_path):
            if not tool_file.endswith(".json"):
                continue
            tool_name = tool_file.replace(".json", "")
            json_path = os.path.join(project_path, tool_file)
            if tool_name == "bandit":
                findings = parse_bandit(json_path)
            elif tool_name == "semgrep":
                findings = parse_semgrep(json_path)
            elif tool_name == "safety":
                findings = parse_safety(json_path)
            elif tool_name == "codeql":
                findings = parse_codeql(json_path)
            else:
                continue
            rows = aggregate_findings(project, tool_name, findings)
            all_rows.extend(rows)

    with open(output_csv, "w", newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(["Project_name", "Tool_name", "CWE_ID", "Number_of_Findings", "Is_In_CWE_Top_25"])
        writer.writerows(all_rows)
    print(f"CSV written to {output_csv}")

if __name__ == "__main__":
    main()