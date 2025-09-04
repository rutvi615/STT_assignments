import matplotlib.pyplot as plt

# -----------------------
# Data from your analysis
# -----------------------
total_commits = 378
merge_commits = 69
non_merge_commits = 309

keywords = {
    "fix": 331,
    "bug": 66,
    "issue": 31,
    "broken": 17,
    "error": 9
}

avg_files_per_commit = 5.40

precise = 2038
vague = 607
neutral = 2433

valid_preds = 4802
invalid_preds = (4802 / 0.946) - 4802  # back-calc total then subtract valid
invalid_preds = int(round(invalid_preds))

valid_rect = 5078
improvements = 1417

file_types = {
    ".py": 2849,
    ".md": 490,
    ".pyc": 421,
    ".txt": 188,
    ".toml": 149
}

# -----------------------
# 1. Bug-fix commit breakdown
# -----------------------
plt.bar(["Total", "Merge", "Non-Merge"], [total_commits, merge_commits, non_merge_commits])
plt.ylabel("Number of Commits")
plt.xlabel("Commit Type")
plt.savefig("commit_breakdown.png", dpi=300, bbox_inches="tight")
plt.close()

# -----------------------
# 2. Keyword frequency
# -----------------------
plt.barh(list(keywords.keys()), list(keywords.values()))
plt.xlabel("Frequency")
plt.ylabel("Keywords")
plt.savefig("keyword_frequency.png", dpi=300, bbox_inches="tight")
plt.close()

# -----------------------
# 3. Average files per commit
# -----------------------
plt.bar(["Average Files"], [avg_files_per_commit])
plt.ylabel("Files per Commit")
plt.savefig("avg_files_per_commit.png", dpi=300, bbox_inches="tight")
plt.close()

# -----------------------
# 4. RQ1 Developer Precision
# -----------------------
labels = ["Precise", "Vague", "Neutral"]
sizes = [precise, vague, neutral]
plt.pie(sizes, labels=labels, autopct="%.1f%%", startangle=140)
plt.savefig("developer_precision.png", dpi=300, bbox_inches="tight")
plt.close()

# -----------------------
# 5. RQ2 LLM Predictions
# -----------------------
plt.pie([valid_preds, invalid_preds], labels=["Valid", "Invalid"], autopct="%.1f%%", startangle=140)
plt.savefig("llm_predictions.png", dpi=300, bbox_inches="tight")
plt.close()

# -----------------------
# 6. RQ3 Rectifier Results
# -----------------------
plt.bar(["Valid Rectifications"], [valid_rect], color="skyblue")
plt.bar(["Improvements"], [improvements], color="orange")
plt.ylabel("Count")
plt.savefig("rectifier_results.png", dpi=300, bbox_inches="tight")
plt.close()

# -----------------------
# 7. File type distribution
# -----------------------
plt.barh(list(file_types.keys()), list(file_types.values()))
plt.xlabel("Frequency")
plt.ylabel("File Types")
plt.savefig("file_types.png", dpi=300, bbox_inches="tight")
plt.close()

print("All plots generated and saved as PNG files")
