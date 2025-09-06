import pandas as pd
import matplotlib.pyplot as plt
from collections import Counter

plt.style.use("seaborn-v0_8-muted")


def main():
    commits_data = pd.read_csv("../lab2/bug_fixing_commits.csv")
    num_commits = len(commits_data)

    modified_files_all = []
    modified_files_count = []

    for entry in commits_data["modified_files"]:
        if isinstance(entry, str):
            try:
                parsed_files = eval(entry)  # Convert string list to actual list
            except Exception:
                parsed_files = [entry]
            modified_files_all.extend(parsed_files)
            modified_files_count.append(len(parsed_files))
        else:
            modified_files_count.append(0)

    num_files = len(modified_files_all)
    avg_files_per_commit = num_files / num_commits if num_commits else 0

    print(f"Commits: {num_commits}")
    print(f"Files: {num_files}")
    print(f"Avg files/commit: {avg_files_per_commit:.2f}")

    # ------------------------------
    # Plot: Summary bar chart
    # ------------------------------
    summary_labels = ["Commits", "Files", "Avg Files/Commit"]
    summary_values = [num_commits, num_files, avg_files_per_commit]

    plt.figure(figsize=(7, 4))
    bars = plt.bar(summary_labels, summary_values,
                   color=["#4C72B0", "#55A868", "#C44E52"],
                   edgecolor="black", alpha=0.85)
    plt.ylabel("Value")
    plt.title("Baseline Summary", fontsize=14, weight="bold")
    plt.grid(axis="y", linestyle="--", alpha=0.6)

    # Add labels inside bars
    for bar in bars:
        height = bar.get_height()
        plt.text(bar.get_x() + bar.get_width() / 2,
                 height * 0.9, f"{height:.1f}",
                 ha="center", va="top", color="white", fontsize=11)

    plt.tight_layout()
    plt.savefig("summary_overview.png")
    plt.close()

    # ------------------------------
    # Plot: Histogram of files per commit
    # ------------------------------
    plt.figure(figsize=(8, 5))
    counts, bins, _ = plt.hist(modified_files_count,
                               bins=range(1, max(modified_files_count) + 2),
                               color="#8172B2", edgecolor="black", alpha=0.8)
    plt.xlabel("Files per Commit")
    plt.ylabel("Number of Commits")
    plt.title("Distribution of Modified Files per Commit", fontsize=14, weight="bold")
    plt.grid(axis="y", linestyle=":", alpha=0.6)

    # Label histogram bars
    for i in range(len(counts)):
        plt.text(bins[i] + 0.5, counts[i] + 0.3, str(int(counts[i])),
                 ha="center", fontsize=9)

    plt.tight_layout()
    plt.savefig("files_per_commit_histogram.png")
    plt.close()

    # ------------------------------
    # Load file-level dataset
    # ------------------------------
    files_data = pd.read_csv("../lab2/commit_predictions.csv")

    # Top file extensions
    extensions = [fname.split(".")[-1] for fname in files_data["File Name"]
                  if isinstance(fname, str) and "." in fname]
    ext_top = Counter(extensions).most_common(8)

    if ext_top:
        ext_labels, ext_freqs = zip(*ext_top)
        plt.figure(figsize=(8, 4))
        bars = plt.bar(ext_labels, ext_freqs,
                       color="#64B5CD", edgecolor="black")
        plt.title("Most Common File Extensions", fontsize=14, weight="bold")
        plt.xlabel("Extension")
        plt.ylabel("Frequency")
        plt.grid(axis="y", linestyle="--", alpha=0.6)

        for bar in bars:
            height = bar.get_height()
            plt.text(bar.get_x() + bar.get_width() / 2,
                     height + 0.3, str(int(height)),
                     ha="center", fontsize=10)

        plt.tight_layout()
        plt.savefig("common_extensions.png")
        plt.close()

    # ------------------------------
    # Top modified filenames
    # ------------------------------
    file_counts = Counter(files_data["File Name"]).most_common(8)
    if file_counts:
        file_labels, file_freqs = zip(*file_counts)
        plt.figure(figsize=(10, 5))
        bars = plt.barh(file_labels, file_freqs,
                        color="#DD8452", edgecolor="black")
        plt.title("Top Modified Filenames", fontsize=14, weight="bold")
        plt.xlabel("Frequency")
        plt.ylabel("Filename")
        plt.grid(axis="x", linestyle="--", alpha=0.6)

        for bar in bars:
            width = bar.get_width()
            plt.text(width + 0.5, bar.get_y() + bar.get_height() / 2,
                     str(int(width)),
                     va="center", fontsize=10)

        plt.tight_layout()
        plt.savefig("common_filenames.png")
        plt.close()

    # ------------------------------
    # Fix type distribution (LLM inference)
    # ------------------------------
    if "LLM Inference (fix type)" in files_data.columns:
        fix_types = [ft for ft in files_data["LLM Inference (fix type)"]
                     if isinstance(ft, str)]
        fix_top = Counter(fix_types).most_common(8)

        if fix_top:
            fix_labels, fix_freqs = zip(*fix_top)
            plt.figure(figsize=(10, 5))
            bars = plt.barh(fix_labels, fix_freqs,
                            color="#55A868", edgecolor="black")
            plt.title("Most Common Fix Types", fontsize=14, weight="bold")
            plt.xlabel("Frequency")
            plt.ylabel("Fix Type")
            plt.grid(axis="x", linestyle="--", alpha=0.6)

            for bar in bars:
                width = bar.get_width()
                plt.text(width + 0.5, bar.get_y() + bar.get_height() / 2,
                         str(int(width)),
                         va="center", fontsize=10)

            plt.tight_layout()
            plt.savefig("fix_type_distribution.png")
            plt.close()


if __name__ == "__main__":
    main()
