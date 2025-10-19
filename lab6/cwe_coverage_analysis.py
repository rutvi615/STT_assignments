#!/usr/bin/env python3
"""
Tool-level CWE Coverage Analysis Script
Analyzes the consolidated security findings to compute CWE coverage by tool.
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from collections import defaultdict
import json

# CWE Top 25 list (2023)
TOP_25_CWE = {
    "CWE-79", "CWE-89", "CWE-787", "CWE-20", "CWE-125", "CWE-78", "CWE-416",
    "CWE-22", "CWE-352", "CWE-434", "CWE-190", "CWE-476", "CWE-502", "CWE-306",
    "CWE-798", "CWE-862", "CWE-276", "CWE-94", "CWE-611", "CWE-863",
    "CWE-732", "CWE-829", "CWE-327", "CWE-200",
    # Support both formats (with and without CWE- prefix)
    "78", "89", "787", "20", "125", "416",
    "22", "352", "434", "190", "476", "502", "306",
    "798", "862", "276", "94", "611", "863",
    "732", "829", "327", "200"
}

def normalize_cwe_id(cwe_id):
    """Normalize CWE ID to consistent format (CWE-XXX)"""
    if cwe_id.startswith("CWE-"):
        return cwe_id
    else:
        return f"CWE-{cwe_id}"

def load_and_analyze_data(csv_file):
    """Load and analyze the consolidated findings CSV"""
    print("📊 Loading consolidated findings...")
    df = pd.read_csv(csv_file)
    
    # Normalize CWE IDs
    df['CWE_ID_Normalized'] = df['CWE_ID'].apply(normalize_cwe_id)
    
    # Check if normalized CWE is in Top 25
    df['Is_Top_25_Normalized'] = df['CWE_ID_Normalized'].isin(TOP_25_CWE)
    
    print(f"✅ Loaded {len(df)} findings across {df['Project_name'].nunique()} projects")
    print(f"🔧 Tools analyzed: {', '.join(df['Tool_name'].unique())}")
    print(f"🎯 Unique CWEs found: {df['CWE_ID_Normalized'].nunique()}")
    
    return df

def analyze_tool_coverage(df):
    """Analyze CWE coverage by each tool"""
    print("\n🔍 Analyzing tool-level CWE coverage...")
    
    coverage_data = {}
    
    for tool in df['Tool_name'].unique():
        tool_df = df[df['Tool_name'] == tool]
        
        # Get unique CWEs detected by this tool
        unique_cwes = set(tool_df['CWE_ID_Normalized'].unique())
        
        # Count Top 25 CWEs detected
        top25_cwes = {cwe for cwe in unique_cwes if cwe in TOP_25_CWE}
        
        # Calculate coverage percentages
        total_cwe_count = len(unique_cwes)
        top25_detected_count = len(top25_cwes)
        top25_coverage_percent = (top25_detected_count / 25) * 100  # Out of 25 possible
        
        # Calculate findings statistics
        total_findings = tool_df['Number_of_Findings'].sum()
        top25_findings = tool_df[tool_df['Is_Top_25_Normalized']]['Number_of_Findings'].sum()
        
        coverage_data[tool] = {
            'unique_cwes': unique_cwes,
            'top25_cwes': top25_cwes,
            'total_cwe_count': total_cwe_count,
            'top25_detected_count': top25_detected_count,
            'top25_coverage_percent': top25_coverage_percent,
            'total_findings': total_findings,
            'top25_findings': top25_findings,
            'top25_findings_percent': (top25_findings / total_findings * 100) if total_findings > 0 else 0
        }
    
    return coverage_data

def print_coverage_summary(coverage_data):
    """Print detailed coverage summary"""
    print("\n" + "="*80)
    print("📈 TOOL-LEVEL CWE COVERAGE ANALYSIS SUMMARY")
    print("="*80)
    
    for tool, data in coverage_data.items():
        print(f"\n🔧 {tool.upper()}")
        print("-" * 50)
        print(f"   Total Unique CWEs Detected: {data['total_cwe_count']}")
        print(f"   Top 25 CWEs Detected: {data['top25_detected_count']}/25")
        print(f"   Top 25 Coverage: {data['top25_coverage_percent']:.1f}%")
        print(f"   Total Findings: {data['total_findings']:,}")
        print(f"   Top 25 Findings: {data['top25_findings']:,} ({data['top25_findings_percent']:.1f}%)")
        
        if data['top25_cwes']:
            print(f"   Top 25 CWEs Found: {', '.join(sorted(data['top25_cwes']))}")
        else:
            print("   Top 25 CWEs Found: None")

def create_visualizations(df, coverage_data):
    """Create comprehensive visualizations"""
    print("\n📊 Generating visualizations...")
    
    # Set up the plotting style
    plt.style.use('default')
    sns.set_palette("husl")
    
    # Create figure with subplots
    fig = plt.figure(figsize=(20, 16))
    
    # 1. Top 25 CWE Coverage by Tool (Bar Chart)
    ax1 = plt.subplot(2, 3, 1)
    tools = list(coverage_data.keys())
    coverage_percentages = [coverage_data[tool]['top25_coverage_percent'] for tool in tools]
    colors = sns.color_palette("husl", len(tools))
    
    bars = ax1.bar(tools, coverage_percentages, color=colors, alpha=0.8, edgecolor='black')
    ax1.set_title('Top 25 CWE Coverage by Tool', fontsize=14, fontweight='bold')
    ax1.set_ylabel('Coverage Percentage (%)', fontsize=12)
    ax1.set_xlabel('Security Tools', fontsize=12)
    ax1.set_ylim(0, max(coverage_percentages) * 1.1 if coverage_percentages else 100)
    
    # Add value labels on bars
    for bar, pct in zip(bars, coverage_percentages):
        height = bar.get_height()
        ax1.text(bar.get_x() + bar.get_width()/2., height + 0.5,
                f'{pct:.1f}%', ha='center', va='bottom', fontweight='bold')
    
    # 2. Total CWE Detection by Tool
    ax2 = plt.subplot(2, 3, 2)
    total_cwes = [coverage_data[tool]['total_cwe_count'] for tool in tools]
    
    bars2 = ax2.bar(tools, total_cwes, color=colors, alpha=0.8, edgecolor='black')
    ax2.set_title('Total Unique CWEs Detected by Tool', fontsize=14, fontweight='bold')
    ax2.set_ylabel('Number of Unique CWEs', fontsize=12)
    ax2.set_xlabel('Security Tools', fontsize=12)
    
    # Add value labels
    for bar, count in zip(bars2, total_cwes):
        height = bar.get_height()
        ax2.text(bar.get_x() + bar.get_width()/2., height + 0.1,
                f'{count}', ha='center', va='bottom', fontweight='bold')
    
    # 3. Findings Distribution (Total vs Top 25)
    ax3 = plt.subplot(2, 3, 3)
    x = np.arange(len(tools))
    width = 0.35
    
    total_findings = [coverage_data[tool]['total_findings'] for tool in tools]
    top25_findings = [coverage_data[tool]['top25_findings'] for tool in tools]
    
    bars3a = ax3.bar(x - width/2, total_findings, width, label='Total Findings', alpha=0.8, color='lightblue', edgecolor='black')
    bars3b = ax3.bar(x + width/2, top25_findings, width, label='Top 25 Findings', alpha=0.8, color='red', edgecolor='black')
    
    ax3.set_title('Security Findings: Total vs Top 25 CWE', fontsize=14, fontweight='bold')
    ax3.set_ylabel('Number of Findings', fontsize=12)
    ax3.set_xlabel('Security Tools', fontsize=12)
    ax3.set_xticks(x)
    ax3.set_xticklabels(tools)
    ax3.legend()
    ax3.set_yscale('log')  # Log scale due to large differences
    
    # 4. CWE Coverage Heatmap
    ax4 = plt.subplot(2, 3, 4)
    
    # Create matrix for heatmap
    all_cwes = set()
    for tool_data in coverage_data.values():
        all_cwes.update(tool_data['unique_cwes'])
    
    # Focus on Top 25 CWEs for readability
    top25_found = {cwe for cwe in all_cwes if cwe in TOP_25_CWE}
    
    if top25_found:
        heatmap_data = []
        for tool in tools:
            row = []
            for cwe in sorted(top25_found):
                if cwe in coverage_data[tool]['unique_cwes']:
                    # Use log of findings count for color intensity
                    findings = df[(df['Tool_name'] == tool) & (df['CWE_ID_Normalized'] == cwe)]['Number_of_Findings'].sum()
                    row.append(np.log10(findings + 1))  # +1 to avoid log(0)
                else:
                    row.append(0)
            heatmap_data.append(row)
        
        heatmap_df = pd.DataFrame(heatmap_data, index=tools, columns=sorted(top25_found))
        sns.heatmap(heatmap_df, annot=True, fmt='.1f', cmap='YlOrRd', ax=ax4, cbar_kws={'label': 'Log10(Findings + 1)'})
        ax4.set_title('Top 25 CWE Detection Heatmap by Tool', fontsize=14, fontweight='bold')
        ax4.set_xlabel('Top 25 CWE IDs', fontsize=12)
        ax4.set_ylabel('Security Tools', fontsize=12)
    else:
        ax4.text(0.5, 0.5, 'No Top 25 CWEs detected', ha='center', va='center', transform=ax4.transAxes)
        ax4.set_title('Top 25 CWE Detection Heatmap', fontsize=14, fontweight='bold')
    
    # 5. Tool Effectiveness Scatter Plot
    ax5 = plt.subplot(2, 3, 5)
    scatter_colors = [colors[i] for i in range(len(tools))]
    
    for i, tool in enumerate(tools):
        ax5.scatter(coverage_data[tool]['total_cwe_count'], 
                   coverage_data[tool]['top25_coverage_percent'],
                   s=coverage_data[tool]['total_findings']/10,  # Size based on findings
                   c=[scatter_colors[i]], 
                   alpha=0.7, 
                   label=tool,
                   edgecolors='black')
    
    ax5.set_title('Tool Effectiveness: Coverage vs Detection', fontsize=14, fontweight='bold')
    ax5.set_xlabel('Total Unique CWEs Detected', fontsize=12)
    ax5.set_ylabel('Top 25 CWE Coverage (%)', fontsize=12)
    ax5.legend()
    ax5.grid(True, alpha=0.3)
    
    # 6. Project-Tool Coverage Matrix
    ax6 = plt.subplot(2, 3, 6)
    
    # Create project-tool matrix
    projects = df['Project_name'].unique()
    project_tool_matrix = []
    
    for project in projects:
        row = []
        for tool in tools:
            project_tool_df = df[(df['Project_name'] == project) & (df['Tool_name'] == tool)]
            if not project_tool_df.empty:
                unique_cwes = project_tool_df['CWE_ID_Normalized'].nunique()
                row.append(unique_cwes)
            else:
                row.append(0)
        project_tool_matrix.append(row)
    
    project_matrix_df = pd.DataFrame(project_tool_matrix, index=projects, columns=tools)
    sns.heatmap(project_matrix_df, annot=True, fmt='d', cmap='Blues', ax=ax6, cbar_kws={'label': 'Unique CWEs'})
    ax6.set_title('CWE Detection by Project-Tool Combination', fontsize=14, fontweight='bold')
    ax6.set_xlabel('Security Tools', fontsize=12)
    ax6.set_ylabel('Projects', fontsize=12)
    
    plt.tight_layout()
    plt.savefig('cwe_coverage_analysis.png', dpi=300, bbox_inches='tight')
    plt.show()
    
    print("✅ Visualizations saved as 'cwe_coverage_analysis.png'")

def export_detailed_analysis(df, coverage_data):
    """Export detailed analysis to files"""
    print("\n💾 Exporting detailed analysis...")
    
    # 1. Tool coverage summary
    coverage_summary = []
    for tool, data in coverage_data.items():
        coverage_summary.append({
            'Tool': tool,
            'Total_Unique_CWEs': data['total_cwe_count'],
            'Top25_CWEs_Detected': data['top25_detected_count'],
            'Top25_Coverage_Percent': round(data['top25_coverage_percent'], 2),
            'Total_Findings': data['total_findings'],
            'Top25_Findings': data['top25_findings'],
            'Top25_Findings_Percent': round(data['top25_findings_percent'], 2),
            'Top25_CWEs_List': ', '.join(sorted(data['top25_cwes']))
        })
    
    coverage_df = pd.DataFrame(coverage_summary)
    coverage_df.to_csv('tool_coverage_summary.csv', index=False)
    
    # 2. Detailed CWE matrix
    all_cwes = set()
    for tool_data in coverage_data.values():
        all_cwes.update(tool_data['unique_cwes'])
    
    cwe_matrix = []
    for cwe in sorted(all_cwes):
        row = {'CWE_ID': cwe, 'Is_Top_25': cwe in TOP_25_CWE}
        for tool in coverage_data.keys():
            detected = cwe in coverage_data[tool]['unique_cwes']
            findings = 0
            if detected:
                findings = df[(df['Tool_name'] == tool) & (df['CWE_ID_Normalized'] == cwe)]['Number_of_Findings'].sum()
            row[f'{tool}_Detected'] = detected
            row[f'{tool}_Findings'] = findings
        cwe_matrix.append(row)
    
    cwe_matrix_df = pd.DataFrame(cwe_matrix)
    cwe_matrix_df.to_csv('cwe_detection_matrix.csv', index=False)
    
    # 3. JSON export for further analysis
    analysis_json = {
        'summary': {
            'total_tools': len(coverage_data),
            'total_unique_cwes': len(all_cwes),
            'top25_cwes_found': len([cwe for cwe in all_cwes if cwe in TOP_25_CWE]),
            'analysis_date': pd.Timestamp.now().isoformat()
        },
        'tool_coverage': coverage_data
    }
    
    # Convert sets to lists for JSON serialization
    for tool_data in analysis_json['tool_coverage'].values():
        tool_data['unique_cwes'] = list(tool_data['unique_cwes'])
        tool_data['top25_cwes'] = list(tool_data['top25_cwes'])
    
    with open('cwe_analysis.json', 'w') as f:
        json.dump(analysis_json, f, indent=2, default=str)
    
    print("✅ Exported files:")
    print("   📊 tool_coverage_summary.csv - Tool coverage metrics")
    print("   🔍 cwe_detection_matrix.csv - Detailed CWE detection matrix")
    print("   📋 cwe_analysis.json - Complete analysis in JSON format")

def main():
    """Main analysis function"""
    print("🚀 Starting Tool-level CWE Coverage Analysis")
    print("="*60)
    
    try:
        # Load and analyze data
        df = load_and_analyze_data('consolidated_findings.csv')
        
        # Analyze tool coverage
        coverage_data = analyze_tool_coverage(df)
        
        # Print summary
        print_coverage_summary(coverage_data)
        
        # Create visualizations
        create_visualizations(df, coverage_data)
        
        # Export detailed analysis
        export_detailed_analysis(df, coverage_data)
        
        print(f"\n🎉 Analysis complete! Check the generated files for detailed results.")
        
    except FileNotFoundError:
        print("❌ Error: consolidated_findings.csv not found!")
        print("   Please ensure the CSV file is in the current directory.")
    except Exception as e:
        print(f"❌ Error during analysis: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    main()