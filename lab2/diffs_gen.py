import csv
import os
from pydriller import Repository

repo_path = "./Ciphey"  # change this to your local path where repo is cloned
codes_dir = "codes"
diffs_dir = "diffs"
os.makedirs(codes_dir, exist_ok=True)
os.makedirs(diffs_dir, exist_ok=True)

with open('commit_diffs.csv', 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
    writer.writerow([
        "Commit Hash",
        "Commit Message",
        "File Name",
        "Source Code Before File Path",
        "Source Code After File Path",
        "Diff File Path"
    ])

    for commit in Repository(repo_path).traverse_commits():
        
        for mod in commit.modified_files:
            before = ""
            after = ""
            diff = ""

            try:
                before = mod.source_code_before or ""
            except Exception:
                before = ""

            try:
                after = mod.source_code or ""
            except Exception:
                after = ""

            try:
                diff = mod.diff or ""
            except Exception:
                diff = ""

            # Create unique filenames for source codes and diff
            base_filename = f"{commit.hash}_{mod.filename}"
            base_filename = base_filename.replace(os.sep, "_").replace("/", "_").replace("\\", "_")
            before_filename = f"{base_filename}_before.txt"
            after_filename = f"{base_filename}_after.txt"
            diff_filename = f"{base_filename}_diff.txt"
            before_path = os.path.join(codes_dir, before_filename)
            after_path = os.path.join(codes_dir, after_filename)
            diff_path = os.path.join(diffs_dir, diff_filename)

            # Write the source codes and diff to their files
            with open(before_path, 'w', encoding='utf-8') as before_file:
                before_file.write(before)
            with open(after_path, 'w', encoding='utf-8') as after_file:
                after_file.write(after)
            with open(diff_path, 'w', encoding='utf-8') as diff_file:
                diff_file.write(diff)

            writer.writerow([
                commit.hash,
                commit.msg,
                mod.filename,
                before_path,
                after_path,
                diff_path
            ])