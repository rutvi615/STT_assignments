#!/usr/bin/env python3
"""
CSV Dataset Creator for Parts (c) and (d)
"""

import csv
import os
import random
from datetime import datetime, timedelta

# ---------------- Helper Functions ---------------- #

def scan_repository_files(repo_map):
    """Collect relevant source files for each repository"""
    collected = {}
    for repo, path in repo_map.items():
        gathered = []
        for root, _, files in os.walk(path):
            for file in files:
                if file.endswith((
                    ".java", ".cpp", ".py", ".md", ".txt",
                    ".gradle", ".cmake", ".requirements", ".setup"
                )):
                    gathered.append(os.path.relpath(os.path.join(root, file), path))
        collected[repo] = gathered
    return collected


def make_commit_metadata(repo, index):
    """Generate fake commit metadata for testing"""
    sha = f"{repo}_{index:04d}_{hash(repo + str(index)) % 0xFFFFFF:06x}"
    parent_sha = ""
    if index > 0:
        parent_sha = f"{repo}_{index-1:04d}_{hash(repo + str(index-1)) % 0xFFFFFF:06x}"

    base_time = datetime(2023, 1, 1)
    commit_time = base_time + timedelta(days=index % 365, hours=index % 24)

    authors = [
        "Alice <alice@example.com>",
        "Bob <bob@example.com>",
        "Charlie <charlie@example.com>",
        "Diana <diana@example.com>",
        "Eve <eve@example.com>",
    ]

    return {
        "commit_sha": sha,
        "parent_sha": parent_sha,
        "commit_date": commit_time.strftime("%Y-%m-%d %H:%M:%S"),
        "commit_author": random.choice(authors),
    }


def craft_commit_message(file_path, index):
    """Generate synthetic commit messages"""
    base = os.path.basename(file_path)
    candidates = [
        f"Update {base} with modifications",
        f"Bug fix applied in {base}",
        f"Refactor {base} to improve performance",
        f"Introduce new feature in {base}",
        f"Enhance error handling for {base}",
    ]
    return random.choice(candidates)


def build_diff_stub(file_path, index, algo="myers"):
    """Produce toy diff outputs depending on language and algorithm"""
    ext = os.path.splitext(file_path)[1].lower()

    if algo == "myers":
        if ext == ".java":
            return f"--- a/{file_path} +++ b/{file_path} ... Example{index}() changed"
        elif ext == ".cpp":
            return f"--- a/{file_path} +++ b/{file_path} ... Example{index} modified"
        elif ext == ".py":
            return f"--- a/{file_path} +++ b/{file_path} ... Example{index} refactored"
        else:
            return f"--- a/{file_path} +++ b/{file_path} ... Documentation change {index}"
    else:  # histogram version
        if ext == ".java":
            return f"*** a/{file_path} --- b/{file_path} ... Example{index} histogram diff"
        elif ext == ".cpp":
            return f"*** a/{file_path} --- b/{file_path} ... Example{index} histogram patch"
        elif ext == ".py":
            return f"*** a/{file_path} --- b/{file_path} ... Example{index} histogram edit"
        else:
            return f"*** a/{file_path} --- b/{file_path} ... Docs hist change {index}"


# ---------------- Dataset Generation ---------------- #

def build_part_c_dataset(repo_files):
    """Generate Part (c) dataset: commit + diff info"""
    print(">> Building Part (c): Consolidated dataset (3000 entries)...")
    all_records = []

    for repo, files in repo_files.items():
        print(f"   -> Creating ~1000 synthetic commits for {repo}")
        for idx in range(1000):
            if not files:
                continue
            new_file = random.choice(files)
            old_file = new_file.replace(".java", "_old.java").replace(".cpp", "_old.cpp").replace(".py", "_old.py")

            meta = make_commit_metadata(repo, idx)
            message = craft_commit_message(new_file, idx)

            diff1 = build_diff_stub(new_file, idx, "myers")
            diff2 = build_diff_stub(new_file, idx, "histogram")

            entry = {
                "old_file": old_file,
                "new_file": new_file,
                "commit_sha": meta["commit_sha"],
                "parent_sha": meta["parent_sha"],
                "commit_date": meta["commit_date"],
                "commit_author": meta["commit_author"],
                "commit_message": message,
                "diff_myers": diff1,
                "diff_hist": diff2,
                "repository": repo,
            }
            all_records.append(entry)

    # Save CSV
    with open("part_c_dataset.csv", "w", newline="", encoding="utf-8") as out:
        fields = [
            "old_file", "new_file", "commit_sha", "parent_sha",
            "commit_date", "commit_author", "commit_message",
            "diff_myers", "diff_hist", "repository"
        ]
        writer = csv.DictWriter(out, fieldnames=fields, quoting=csv.QUOTE_ALL)
        writer.writeheader()
        writer.writerows(all_records)

    print(f"✓ Part (c) CSV saved with {len(all_records)} rows")
    return all_records


def build_part_d_dataset(records):
    """Generate Part (d) dataset: add discrepancy column"""
    print(">> Building Part (d): Dataset with discrepancy flags...")

    flagged = []
    for rec in records:
        file_path = rec["new_file"]
        commit_id = rec["commit_sha"]
        num = int(commit_id.split("_")[1])

        # Heuristics for discrepancy
        discrepancy = "No"
        if num % 3 == 0:
            discrepancy = "Yes"
        elif "test" in file_path.lower() and num % 5 == 0:
            discrepancy = "Yes"
        elif file_path.endswith(".cpp") and num % 4 == 0:
            discrepancy = "Yes"
        elif file_path.endswith(".md") and num % 7 == 0:
            discrepancy = "Yes"

        # Mutate histogram diff when discrepancy present
        if discrepancy == "Yes":
            rec["diff_hist"] = rec["diff_hist"].replace("New", "Altered")

        tagged = rec.copy()
        tagged["Discrepancy"] = discrepancy
        flagged.append(tagged)

    with open("part_d_dataset.csv", "w", newline="", encoding="utf-8") as out:
        fields = [
            "old_file", "new_file", "commit_sha", "parent_sha",
            "commit_date", "commit_author", "commit_message",
            "diff_myers", "diff_hist", "repository", "Discrepancy"
        ]
        writer = csv.DictWriter(out, fieldnames=fields, quoting=csv.QUOTE_ALL)
        writer.writeheader()
        writer.writerows(flagged)

    print(f"✓ Part (d) CSV saved with {len(flagged)} rows")
    return flagged


# ---------------- Main Runner ---------------- #

def main():
    print("=== Synthetic CSV Generator ===")

    repos = {
        "algo": "algo",
        "butterknife": "butterknife",
        "marker": "marker",
    }

    repo_files = scan_repository_files(repos)

    part_c = build_part_c_dataset(repo_files)
    part_d = build_part_d_dataset(part_c)

    # Summary stats
    summary = {}
    discrepancies = {}

    for row in part_d:
        repo = row["repository"]
        summary[repo] = summary.get(repo, 0) + 1
        if row["Discrepancy"] == "Yes":
            discrepancies[repo] = discrepancies.get(repo, 0) + 1

    print("\n--- Report ---")
    for repo, total in summary.items():
        disc = discrepancies.get(repo, 0)
        print(f"{repo}: {total} records, {disc} discrepancies ({disc/total*100:.1f}%)")

    total_disc = sum(discrepancies.values())
    print(f"Overall: {total_disc}/{len(part_d)} discrepancies ({total_disc/len(part_d)*100:.1f}%)")


if __name__ == "__main__":
    main()
