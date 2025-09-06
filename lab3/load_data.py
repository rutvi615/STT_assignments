import os
import pandas as pd

LAB2_DIR = os.path.join(os.path.dirname(__file__), '..', 'Lab2')
CODES_DIR = os.path.join(LAB2_DIR, 'codes')

# Load commit-level dataset
def load_commit_dataset():
    path = os.path.join(LAB2_DIR, 'bug_fixing_commits.csv')
    print(f"📂 Loading commit dataset: {path}")
    if not os.path.exists(path):
        print("❌ File not found!")
    return pd.read_csv(path)

# Load file-level dataset
def load_file_dataset():
    path = os.path.join(LAB2_DIR, 'commit_predictions.csv')
    print(f"📂 Loading file dataset: {path}")
    if not os.path.exists(path):
        print("❌ File not found!")
    return pd.read_csv(path)

def get_code_pair(commit_hash, filename):
    base = os.path.basename(filename)
    before_path = os.path.join(CODES_DIR, f"{commit_hash}_{base}_before.txt")
    after_path  = os.path.join(CODES_DIR, f"{commit_hash}_{base}_after.txt")

    code_before = None
    code_after = None

    # Load BEFORE file only if it has content
    if os.path.exists(before_path):
        with open(before_path, encoding='utf-8') as f:
            content = f.read().strip()
            if content:
                code_before = content
                print(f"✅ Loaded BEFORE file: {before_path} ({len(code_before.splitlines())} lines)")
            else:
                print(f"⚠️ BEFORE file empty → skipping: {before_path}")
    else:
        print(f"⚠️ BEFORE file missing: {before_path}")

    # Load AFTER file (always if exists)
    if os.path.exists(after_path):
        with open(after_path, encoding='utf-8') as f:
            code_after = f.read()
        print(f"✅ Loaded AFTER file: {after_path} ({len(code_after.splitlines())} lines)")
    else:
        print(f"⚠️ AFTER file missing: {after_path}")

    return code_before, code_after


# Utility to read a diff file
def get_diff_content(diff_path):
    if not os.path.isabs(diff_path):
        base_dir = os.path.join(os.path.dirname(__file__), '..', 'Lab2', 'diffs')
        full_path = os.path.join(base_dir, diff_path)
    else:
        full_path = diff_path

    if os.path.exists(full_path):
        with open(full_path, encoding='utf-8') as f:
            diff = f.read()
        print(f"✅ Loaded DIFF file: {full_path} ({len(diff.splitlines())} lines)")
        return diff
    else:
        print(f"⚠️ Diff file missing: {full_path}")
    return None
if __name__ == "__main__":
    print("🔍 Debugging load_data.py")

    # Load datasets
    file_df = load_file_dataset()
    print(f"Loaded {len(file_df)} rows from commit_predictions.csv")
    print(file_df.head(), "\n")

    # Test loading code files for the first row
    commit_hash = file_df.iloc[0]["Commit Hash"]
    filename = file_df.iloc[0]["File Name"]

    print(f"➡️ Trying to load code pair for: {filename} (hash: {commit_hash})")
    code_before, code_after = get_code_pair(commit_hash, filename)

    print("\n--- Code Before (first 200 chars) ---")
    print(code_before[:200] if code_before else "❌ No BEFORE code loaded")

    print("\n--- Code After (first 200 chars) ---")
    print(code_after[:200] if code_after else "❌ No AFTER code loaded")
