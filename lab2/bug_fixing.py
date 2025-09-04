import csv
from pydriller import Repository

# Target repository
repo_url = "https://github.com/bee-san/Ciphey"
output_file = "bug_fixing_commits.csv"

# Expanded keyword list
keywords = [
    "fixed ", " bug", "fixes ", "fix", "fix", " fixed", " fixes", "crash", "solves", " resolves", "resolves",
    "issue", "issue ", "regression", "fall back", "assertion", "coverity", "reproducible", "stack-wanted",
    "steps-wanted", "testcase", "failur", "fail", "npe ", " npe", "except", "broken", "differential testing",
    "error", "hang ", " hang", "test fix", "steps to reproduce", "crash", "assertion", "failure", "leak",
    "stack trace", "heap overflow", "freez", "problem", "problem", "overflow", "overflow ", "avoid ", "avoid",
    "workaround ", "workaround", "break", "break", "stop", "stop"
]

with open(output_file, "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["hash", "message", "parents", "is_merge", "modified_files"])

    for commit in Repository(repo_url).traverse_commits():
        msg = commit.msg.lower()
        if any(kw in msg for kw in keywords):
            writer.writerow([
                commit.hash,
                commit.msg,
                commit.parents,
                commit.merge,
                [m.new_path for m in commit.modified_files]
            ])

print(f"Done! Bug-fixing commits stored in {output_file}")
