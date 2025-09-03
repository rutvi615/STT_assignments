#!/usr/bin/env python3
"""
Part (e) - Statistical Analysis of Final Dataset
"""

import pandas as pd

def classify_file(filepath):
    """Identify the type of file based on its path/name"""
    if pd.isna(filepath) or filepath.strip() == "":
        return "Source Code"

    path = filepath.lower()
    if "readme" in path or path.endswith(".md"):
        return "README"
    elif "license" in path or "licence" in path:
        return "LICENSE"
    elif any(tag in path for tag in ["test", "spec", "_test"]):
        return "Test Code"
    else:
        return "Source Code"

def perform_statistics():
    print("=" * 70)
    print("PART (e): ANALYZING FINAL DATASET STATISTICS")
    print("=" * 70)

    try:
        dataset = pd.read_csv("part_d_dataset.csv")
        print(f" Loaded dataset with {len(dataset)} rows and {len(dataset.columns)} columns")
    except Exception as err:
        print(f" Could not load dataset: {err}")
        return

    # Initialize counters
    mismatch_by_type = {
        "Source Code": 0,
        "Test Code": 0,
        "README": 0,
        "LICENSE": 0
    }

    filetype_counts = {
        "Source Code": 0,
        "Test Code": 0,
        "README": 0,
        "LICENSE": 0
    }

    # Process each file
    for _, row in dataset.iterrows():
        ftype = classify_file(row["new_file"])
        filetype_counts[ftype] += 1
        if row["Discrepancy"] == "Yes":
            mismatch_by_type[ftype] += 1

    # Print mismatch statistics
    print("\n FILETYPE-BASED MISMATCH STATISTICS:")
    print("-" * 50)
    for ftype, mismatches in mismatch_by_type.items():
        print(f"Mismatches in {ftype}: {mismatches}")

    # Overall dataset statistics
    discrepancy_summary = dataset["Discrepancy"].value_counts()
    mismatched = discrepancy_summary.get("Yes", 0)
    clean = discrepancy_summary.get("No", 0)

    print("\n OVERALL SUMMARY:")
    print(f"Total files checked: {len(dataset)}")
    print(f"Files with discrepancies: {mismatched}")
    print(f"Files without discrepancies: {clean}")
    print(f"Overall mismatch rate: {(mismatched / len(dataset)) * 100:.1f}%")

    # Repo-wise discrepancy breakdown
    print("\n REPOSITORY STATISTICS:")
    repo_discrepancies = dataset.groupby("repository")["Discrepancy"].apply(lambda x: (x == "Yes").sum())
    repo_totals = dataset["repository"].value_counts()

    for repo in repo_discrepancies.index:
        mism = repo_discrepancies[repo]
        total = repo_totals[repo]
        perc = (mism / total) * 100
        print(f"{repo}: {mism}/{total} discrepancies ({perc:.1f}%)")

    # File distribution
    print("\n FILETYPE DISTRIBUTION:")
    for ftype, count in filetype_counts.items():
        percent = (count / len(dataset)) * 100
        print(f"  {ftype}: {count} files ({percent:.1f}%)")

    print("\n" + "=" * 70)
    print("STATISTICS PROCESSING COMPLETE")
    print("=" * 70)

def main():
    print(">>> Running Statistics Module <<<")
    perform_statistics()

if __name__ == "__main__":
    main()
