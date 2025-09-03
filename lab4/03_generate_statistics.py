#!/usr/bin/env python3
"""
Part (e) - Generate Six Graphs for Final Report
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# -------------------------------
# Helper Function
# -------------------------------
def classify_filetype(path):
    """Classify file into type categories"""
    if pd.isna(path) or path.strip() == "":
        return "Source Code"
    path = path.lower()
    if "readme" in path or path.endswith(".md"):
        return "README"
    elif "license" in path or "licence" in path:
        return "LICENSE"
    elif any(marker in path for marker in ["test", "spec", "_test"]):
        return "Test Code"
    else:
        return "Source Code"

# -------------------------------
# Graph Functions
# -------------------------------
def plot1_mismatches_vs_filetype(df):
    print("➡ Generating Graph 1 (Mismatches by File Type)...")

    mismatch_counts = {"Source Code": 0, "Test Code": 0, "README": 0, "LICENSE": 0}

    for _, row in df.iterrows():
        category = classify_filetype(row["new_file"])
        if row["Discrepancy"] == "Yes":
            mismatch_counts[category] += 1

    plt.figure(figsize=(10, 7))
    keys, values = list(mismatch_counts.keys()), list(mismatch_counts.values())
    bars = plt.bar(keys, values, color=["#E74C3C", "#27AE60", "#2980B9", "#F1C40F"], alpha=0.85)

    plt.title("Graph 1 - Discrepancies by File Type", fontsize=15, weight="bold")
    plt.xlabel("File Categories", fontsize=13, weight="bold")
    plt.ylabel("Mismatched Files", fontsize=13, weight="bold")
    plt.grid(axis="y", linestyle=":", alpha=0.5)

    for bar in bars:
        plt.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 3,
                 str(int(bar.get_height())), ha="center", fontsize=11, weight="bold")

    plt.savefig("graph1_filetype_mismatches.png", dpi=300, bbox_inches="tight")
    plt.close()
    print("✔ Graph 1 saved.")

def plot2_overall_distribution(df):
    print("➡ Generating Graph 2 (Overall Distribution)...")

    counts = df["Discrepancy"].value_counts()
    plt.figure(figsize=(7, 7))

    wedges, texts, autotexts = plt.pie(
        counts,
        labels=[f"{lbl} ({cnt})" for lbl, cnt in zip(counts.index, counts.values)],
        autopct="%1.1f%%",
        startangle=120,
        explode=[0.07] * len(counts),
        colors=["#2ECC71", "#E74C3C"],
        textprops={"fontsize": 11}
    )

    for a in autotexts:
        a.set_fontsize(12)
        a.set_weight("bold")
        a.set_color("white")

    plt.title("Graph 2 - Myers vs Histogram (Discrepancy Split)", fontsize=15, weight="bold")
    plt.savefig("graph2_distribution.png", dpi=300, bbox_inches="tight")
    plt.close()
    print("✔ Graph 2 saved.")

def plot3_repo_wise(df):
    print("➡ Generating Graph 3 (Repository Analysis)...")

    repo_mismatches = df.groupby("repository")["Discrepancy"].apply(lambda x: (x == "Yes").sum())
    repo_totals = df["repository"].value_counts()

    plt.figure(figsize=(10, 6))
    bars = plt.bar(repo_mismatches.index, repo_mismatches.values, color=["#3498DB", "#9B59B6", "#E67E22"])

    plt.title("Graph 3 - Mismatches by Repository", fontsize=15, weight="bold")
    plt.ylabel("Number of Discrepancies", fontsize=13, weight="bold")
    plt.xlabel("Repositories", fontsize=13, weight="bold")
    plt.grid(axis="y", linestyle="--", alpha=0.5)

    for i, bar in enumerate(bars):
        total = repo_totals[repo_mismatches.index[i]]
        pct = (bar.get_height() / total) * 100
        plt.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 2,
                 f"{bar.get_height()} ({pct:.1f}%)", ha="center", fontsize=10, weight="bold")

    plt.savefig("graph3_repo_mismatches.png", dpi=300, bbox_inches="tight")
    plt.close()
    print("✔ Graph 3 saved.")

def plot4_filetype_distribution(df):
    print("➡ Generating Graph 4 (File Type Distribution)...")

    counts = {"Source Code": 0, "Test Code": 0, "README": 0, "LICENSE": 0}
    for _, row in df.iterrows():
        counts[classify_filetype(row["new_file"])] += 1

    plt.figure(figsize=(9, 6))
    bars = plt.bar(counts.keys(), counts.values(), color=["#8E44AD", "#1ABC9C", "#F39C12", "#C0392B"], alpha=0.85)

    plt.title("Graph 4 - File Type Distribution", fontsize=15, weight="bold")
    plt.xlabel("File Types", fontsize=13, weight="bold")
    plt.ylabel("File Count", fontsize=13, weight="bold")

    for bar in bars:
        perc = (bar.get_height() / len(df)) * 100
        plt.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 5,
                 f"{bar.get_height()} ({perc:.1f}%)", ha="center", fontsize=10, weight="bold")

    plt.savefig("graph4_filetypes.png", dpi=300, bbox_inches="tight")
    plt.close()
    print("✔ Graph 4 saved.")

def plot5_algo_results(df):
    print("➡ Generating Graph 5 (Algorithm Comparison)...")

    mismatch = df["Discrepancy"].value_counts().get("Yes", 0)
    match = df["Discrepancy"].value_counts().get("No", 0)

    plt.figure(figsize=(8, 6))
    labels = ["Matching Results", "Different Results"]
    bars = plt.bar(labels, [match, mismatch], color=["#16A085", "#C0392B"])

    plt.title("Graph 5 - Algorithm Agreement vs Disagreement", fontsize=15, weight="bold")
    plt.ylabel("Files Count", fontsize=13, weight="bold")

    total = len(df)
    for i, bar in enumerate(bars):
        val = bar.get_height()
        perc = (val / total) * 100
        plt.text(bar.get_x() + bar.get_width()/2, val + 2,
                 f"{val} ({perc:.1f}%)", ha="center", fontsize=11, weight="bold")

    plt.savefig("graph5_algo_results.png", dpi=300, bbox_inches="tight")
    plt.close()
    print("✔ Graph 5 saved.")

def plot6_repo_discrepancy_rate(df):
    print("➡ Generating Graph 6 (Repo Discrepancy Rate)...")

    repo_mismatches = df.groupby("repository")["Discrepancy"].apply(lambda x: (x == "Yes").sum())
    repo_totals = df["repository"].value_counts()
    rates = [(repo_mismatches[r] / repo_totals[r]) * 100 for r in repo_mismatches.index]

    plt.figure(figsize=(10, 6))
    bars = plt.bar(repo_mismatches.index, rates, color=["#E74C3C", "#2ECC71", "#9B59B6"])

    plt.title("Graph 6 - Discrepancy Rate by Repository", fontsize=15, weight="bold")
    plt.ylabel("Rate (%)", fontsize=13, weight="bold")

    avg_rate = np.mean(rates)
    plt.axhline(y=avg_rate, color="black", linestyle="--", linewidth=1)
    plt.text(0, avg_rate + 1, f"Avg: {avg_rate:.1f}%", fontsize=10, weight="bold")

    for i, bar in enumerate(bars):
        plt.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 1,
                 f"{rates[i]:.1f}%", ha="center", fontsize=10, weight="bold")

    plt.savefig("graph6_repo_rates.png", dpi=300, bbox_inches="tight")
    plt.close()
    print("✔ Graph 6 saved.")

# -------------------------------
# Main Runner
# -------------------------------
def main():
    print("Part (e): Generating All Graphs")
    print("=" * 50)

    try:
        data = pd.read_csv("part_d_dataset.csv")
        print(f"Dataset Loaded Successfully: {len(data)} rows")
    except Exception as e:
        print(f"Error: {e}")
        print("Run the dataset preparation script first.")
        return

    plt.style.use("ggplot")

    plot1_mismatches_vs_filetype(data)
    plot2_overall_distribution(data)
    plot3_repo_wise(data)
    plot4_filetype_distribution(data)
    plot5_algo_results(data)
    plot6_repo_discrepancy_rate(data)

    print("\n All six graphs generated successfully!")

if __name__ == "__main__":
    main()
