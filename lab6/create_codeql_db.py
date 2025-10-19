import os
import subprocess

def create_codeql_db(repo_path, db_path):
    codeql_path = r"D:/setup/codeql/codeql.exe"  # Use your actual path
    subprocess.run([
        codeql_path, "database", "create", db_path,
        "--language=python", "--source-root", repo_path, "--overwrite"
    ], check=False)

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
        db_path = os.path.join(project_results, "codeql-db")
        print(f"Creating CodeQL DB for {project}...")
        create_codeql_db(repo_path, db_path)
        print()

if __name__ == "__main__":
    main()
