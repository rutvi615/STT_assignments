#!/usr/bin/env python3
"""
Lab 2 Analysis Script (Ciphey Repository)
Performs lightweight commit analysis and generates a markdown report
"""

import pandas as pd
import numpy as np
from collections import Counter
from datetime import datetime
import os

def run_analysis():
    """Load CSV data and perform commit analysis"""
    print("Loading datasets for analysis...")

    # Load bug-fixing commits
    try:
        bug_data = pd.read_csv('bug_fixing_commits.csv')
        print(f"✓ {len(bug_data)} bug-fixing commits loaded")
    except Exception as e:
        print(f"✗ Could not read bug_fixing_commits.csv: {e}")
        return None, None

    # Load prediction data
    try:
        pred_data = pd.read_csv('commit_predictions.csv')
        print(f"✓ {len(pred_data)} commit predictions loaded")
    except Exception as e:
        print(f"✗ Could not read commit_predictions.csv: {e}")
        return None, None

    print("\n" + "="*60)
    print("CIPHEY REPOSITORY ANALYSIS")
    print("="*60)

    ciphey_stats = {
        'Repository': 'Ciphey',
        'GitHub Stars': '4.4k+',
        'Forks': '240+',
        'Contributors': '50+',
        'Primary Language': 'Python',
        'License': 'MIT',
        'Age': '5+ years'
    }

    print("Repository chosen: Ciphey")
    print("Why Ciphey?")
    print("1. ✓ Actively used in real-world security applications")
    print("2. ✓ Medium-size project with meaningful commit history")
    print("3. ✓ Maintained by an active open-source community")
    print("4. ✓ Clear bug-fix history for analysis")
    print("5. ✓ Popularity and real-world relevance")

    # Bug-fix stats
    total_commits = len(bug_data)
    merge_count = bug_data['Is a merge commit?'].sum()
    non_merge_count = total_commits - merge_count

    print(f"\nTotal bug-fix commits: {total_commits}")
    print(f"Merge commits: {merge_count}")
    print(f"Non-merge commits: {non_merge_count}")

    # Keyword frequency
    keywords = ["fix", "bug", "error", "crash", "issue", "problem", "broken"]
    kw_freq = {k: bug_data['Message'].str.lower().str.contains(k, na=False).sum() for k in keywords}

    print("\nMost frequent bug-related terms:")
    for k, v in sorted(kw_freq.items(), key=lambda x: x[1], reverse=True)[:5]:
        print(f"  {k}: {v}")

    # Files modified per commit
    file_counts = []
    for row in bug_data['List of modified files']:
        try:
            parsed = eval(row) if pd.notna(row) else []
            file_counts.append(len(parsed))
        except:
            file_counts.append(0)

    avg_files = np.mean(file_counts)
    print(f"\nAverage number of files per commit: {avg_files:.2f}")

    # RQ1: Developer message precision
    dev_msgs = pred_data['Commit Message'].tolist()
    precise_ind = ["fix", "bug", "error", "issue", "crash"]
    vague_ind = ["update", "change", "modify", "refactor"]

    precise, vague, neutral = 0, 0, 0
    for msg in dev_msgs:
        if pd.isna(msg):
            neutral += 1
            continue
        lower = msg.lower()
        if any(word in lower for word in precise_ind):
            precise += 1
        elif any(word in lower for word in vague_ind):
            vague += 1
        else:
            neutral += 1

    dev_precision = precise / len(dev_msgs) * 100

    print("\nRQ1 Developer Precision:")
    print(f"Precise: {precise} ({dev_precision:.1f}%)")
    print(f"Vague: {vague} ({vague/len(dev_msgs)*100:.1f}%)")
    print(f"Neutral: {neutral} ({neutral/len(dev_msgs)*100:.1f}%)")

    # RQ2: LLM success rate
    llm_preds = pred_data['LLM Inference (fix type)'].tolist()
    good_preds = sum(1 for p in llm_preds if pd.notna(p) and str(p).strip() not in ('', 'nan'))
    llm_rate = good_preds / len(llm_preds) * 100

    print("\nRQ2 LLM Predictions:")
    print(f"Valid predictions: {good_preds} ({llm_rate:.1f}%)")

    # RQ3: Rectification success
    rectified = pred_data['Rectified Message'].tolist()
    improved, valid = 0, 0
    for orig, rect in zip(dev_msgs, rectified):
        if pd.notna(rect) and str(rect).strip() not in ('', 'nan'):
            valid += 1
            if len(str(rect).strip()) > len(str(orig).strip()) * 0.8:
                improved += 1

    rect_rate = improved / len(rectified) * 100

    print("\nRQ3 Rectifier Results:")
    print(f"Valid rectifications: {valid} ({valid/len(rectified)*100:.1f}%)")
    print(f"Improvements: {improved} ({rect_rate:.1f}%)")

    # File type distribution
    file_exts = []
    for f in pred_data['File Name']:
        if pd.notna(f) and '.' in str(f):
            file_exts.append(str(f).split('.')[-1].lower())
        else:
            file_exts.append('no_extension')
    
    ext_counts = Counter(file_exts)
    print("\nTop modified file types:")
    for ext, count in ext_counts.most_common(5):
        print(f"  .{ext}: {count}")

    results = {
        'total_bug_commits': total_commits,
        'merge_commits': merge_count,
        'avg_files_per_commit': avg_files,
        'developer_precision_rate': dev_precision,
        'llm_success_rate': llm_rate,
        'rectification_rate': rect_rate,
        'top_keywords': dict(sorted(kw_freq.items(), key=lambda x: x[1], reverse=True)[:5]),
        'top_file_types': dict(ext_counts.most_common(5))
    }

    return results, ciphey_stats

def make_report(results, repo_stats):
    """Generate a markdown report from results"""
    return f"""# Lab Assignment 2 - Report
## CS202 Software Tools & Techniques
### Repository: {repo_stats['Repository']}
### Date: {datetime.now().strftime('%B %d, %Y')}

---

### Repository Overview
- Stars: {repo_stats['GitHub Stars']}
- Forks: {repo_stats['Forks']}
- Contributors: {repo_stats['Contributors']}
- Language: {repo_stats['Primary Language']}
- License: {repo_stats['License']}
- Age: {repo_stats['Age']}

### Bug-Fix Commit Stats
- Total bug-fix commits: {results['total_bug_commits']}
- Merge commits: {results['merge_commits']}
- Avg files per commit: {results['avg_files_per_commit']:.2f}

### Keyword Frequency
{results['top_keywords']}

### RQ1 Developer Precision
- Precision rate: {results['developer_precision_rate']:.1f}%

### RQ2 LLM Generation
- Success rate: {results['llm_success_rate']:.1f}%

### RQ3 Rectification
- Improvement rate: {results['rectification_rate']:.1f}%

### File Types
{results['top_file_types']}

*Report auto-generated on {datetime.now().strftime('%B %d, %Y at %I:%M %p')}*
"""

def main():
    print("Starting analysis for Ciphey repo...")
    results, stats = run_analysis()
    if results:
        md = make_report(results, stats)
        with open('Lab2_Report_Ciphey.md', 'w', encoding='utf-8') as f:
            f.write(md)
        print("\n Report generated: Lab2_Report_Ciphey.md")
    else:
        print("Analysis failed")

if __name__ == "__main__":
    main()
