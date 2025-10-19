#!/usr/bin/env python3
"""
Simplified CWE Coverage Analysis with Key Insights
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

def create_summary_report():
    """Create a comprehensive summary report"""
    
    print("="*80)
    print("🎯 TOOL-LEVEL CWE COVERAGE ANALYSIS - KEY INSIGHTS")
    print("="*80)
    
    # Load the summary data
    df = pd.read_csv('tool_coverage_summary.csv')
    
    print("\n📊 COVERAGE METRICS SUMMARY:")
    print("-" * 50)
    for _, row in df.iterrows():
        print(f"\n🔧 {row['Tool'].upper()}:")
        print(f"   • Unique CWEs Detected: {row['Total_Unique_CWEs']}")
        print(f"   • Top 25 CWE Coverage: {row['Top25_Coverage_Percent']}% ({row['Top25_CWEs_Detected']}/25)")
        print(f"   • Total Security Findings: {row['Total_Findings']:,}")
        print(f"   • Critical Findings (Top 25): {row['Top25_Findings']} ({row['Top25_Findings_Percent']:.1f}%)")
        if row['Top25_CWEs_List']:
            print(f"   • Top 25 CWEs Found: {row['Top25_CWEs_List']}")
    
    # Rankings
    print(f"\n🏆 TOOL RANKINGS:")
    print("-" * 30)
    
    # Rank by Top 25 coverage
    df_sorted = df.sort_values('Top25_Coverage_Percent', ascending=False)
    print("\n📈 By Top 25 CWE Coverage:")
    for i, (_, row) in enumerate(df_sorted.iterrows(), 1):
        print(f"   {i}. {row['Tool']}: {row['Top25_Coverage_Percent']:.1f}%")
    
    # Rank by total CWEs
    df_sorted = df.sort_values('Total_Unique_CWEs', ascending=False)
    print("\n🔍 By Total CWE Detection:")
    for i, (_, row) in enumerate(df_sorted.iterrows(), 1):
        print(f"   {i}. {row['Tool']}: {row['Total_Unique_CWEs']} CWEs")
    
    # Rank by findings volume
    df_sorted = df.sort_values('Total_Findings', ascending=False)
    print("\n📋 By Total Findings Volume:")
    for i, (_, row) in enumerate(df_sorted.iterrows(), 1):
        print(f"   {i}. {row['Tool']}: {row['Total_Findings']:,} findings")

def create_key_visualizations():
    """Create separate, focused visualizations"""
    
    df = pd.read_csv('tool_coverage_summary.csv')
    
    # Colors for consistency
    colors = ['#FF6B6B', '#4ECDC4', '#45B7D1']
    
    # 1. Top 25 CWE Coverage Comparison (Pie Chart)
    plt.figure(figsize=(10, 8))
    
    # Calculate coverage data for pie chart
    coverage_data = df['Top25_Coverage_Percent'].tolist()
    tool_names = df['Tool'].tolist()
    
    # Create labels with percentages
    labels = [f'{tool}\n{coverage}%' for tool, coverage in zip(tool_names, coverage_data)]
    
    # Create pie chart
    wedges, texts, autotexts = plt.pie(coverage_data, labels=labels, colors=colors, 
                                       autopct='%1.1f%%', startangle=90,
                                       explode=(0.05, 0.05, 0.05),  # Slightly separate slices
                                       shadow=True, textprops={'fontsize': 11, 'fontweight': 'bold'})
    
    plt.title('Top 25 CWE Coverage Distribution by Security Tool', fontweight='bold', fontsize=16, pad=20)
    
    # Improve text visibility
    for autotext in autotexts:
        autotext.set_color('white')
        autotext.set_fontweight('bold')
        autotext.set_fontsize(12)
    
    plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle
    plt.tight_layout()
    plt.savefig('plot1_top25_coverage.png', dpi=300, bbox_inches='tight')
    plt.show()
    
    # 2. Total vs Top 25 Findings Comparison
    plt.figure(figsize=(12, 7))
    x = np.arange(len(df['Tool']))
    width = 0.35
    
    bars1 = plt.bar(x - width/2, df['Total_Findings'], width, label='Total Findings', 
                   color='lightblue', alpha=0.8, edgecolor='black', linewidth=1.5)
    bars2 = plt.bar(x + width/2, df['Top25_Findings'], width, label='Top 25 CWE Findings', 
                   color='red', alpha=0.8, edgecolor='black', linewidth=1.5)
    
    plt.title('Security Findings Volume: Total vs Top 25 CWE', fontweight='bold', fontsize=16, pad=20)
    plt.ylabel('Number of Findings (Log Scale)', fontsize=12)
    plt.xlabel('Security Tools', fontsize=12)
    plt.yscale('log')
    plt.xticks(x, df['Tool'])
    plt.legend(fontsize=11)
    plt.grid(axis='y', alpha=0.3, linestyle='--')
    
    # Add value labels on bars
    for i, (total, top25) in enumerate(zip(df['Total_Findings'], df['Top25_Findings'])):
        plt.text(i - width/2, total * 1.1, f'{total:,}', ha='center', fontweight='bold', fontsize=10)
        plt.text(i + width/2, top25 * 1.1, f'{top25}', ha='center', fontweight='bold', fontsize=10)
    
    plt.tight_layout()
    plt.savefig('plot2_findings_volume.png', dpi=300, bbox_inches='tight')
    plt.show()
    
    # 3. Tool Effectiveness Matrix (Bubble Chart)
    plt.figure(figsize=(12, 8))
    
    for i, row in df.iterrows():
        bubble_size = max(100, row['Total_Findings']/10)  # Minimum size for visibility
        plt.scatter(row['Total_Unique_CWEs'], row['Top25_Coverage_Percent'], 
                   s=bubble_size, c=[colors[i]], alpha=0.7, 
                   edgecolor='black', linewidth=2, label=row['Tool'])
        
        # Add tool name annotations
        plt.annotate(f"{row['Tool']}\n({row['Total_Findings']:,} findings)", 
                    (row['Total_Unique_CWEs'], row['Top25_Coverage_Percent']),
                    xytext=(10, 10), textcoords='offset points', 
                    fontweight='bold', fontsize=11,
                    bbox=dict(boxstyle='round,pad=0.3', facecolor=colors[i], alpha=0.3))
    
    plt.title('Tool Effectiveness Matrix\n(Bubble Size = Total Findings Volume)', fontweight='bold', fontsize=16, pad=20)
    plt.xlabel('Total Unique CWEs Detected', fontsize=12)
    plt.ylabel('Top 25 CWE Coverage (%)', fontsize=12)
    plt.grid(True, alpha=0.3)
    plt.legend()
    plt.tight_layout()
    plt.savefig('plot3_effectiveness_matrix.png', dpi=300, bbox_inches='tight')
    plt.show()
    
    # 4. Top 25 CWE Detection Heatmap
    create_cwe_heatmap()
    
    # 5. Coverage Gaps Analysis
    create_coverage_gaps_plot()
    
    print("✅ Individual visualizations saved:")
    print("   📊 plot1_top25_coverage.png - Top 25 CWE coverage pie chart")
    print("   📊 plot2_findings_volume.png - Total vs Top 25 findings volume")  
    print("   📊 plot3_effectiveness_matrix.png - Tool effectiveness matrix")
    print("   📊 plot4_cwe_heatmap.png - Top 25 CWE detection heatmap")
    print("   📊 plot5_coverage_gaps.png - Coverage gaps analysis")

def create_cwe_heatmap():
    """Create a heatmap showing Top 25 CWE detection by tool"""
    
    # Load the consolidated findings data
    df_consolidated = pd.read_csv('consolidated_findings.csv')
    df_tools = pd.read_csv('tool_coverage_summary.csv')
    
    # Normalize CWE IDs
    def normalize_cwe_id(cwe_id):
        if str(cwe_id).startswith("CWE-"):
            return str(cwe_id)
        else:
            return f"CWE-{cwe_id}"
    
    df_consolidated['CWE_ID_Normalized'] = df_consolidated['CWE_ID'].apply(normalize_cwe_id)
    
    # Get tools and all detected Top 25 CWEs
    tools = df_tools['Tool'].tolist()
    
    # Standard Top 25 CWEs 
    TOP_25_CWE = {
        "CWE-79", "CWE-89", "CWE-787", "CWE-20", "CWE-125", "CWE-78", "CWE-416",
        "CWE-22", "CWE-352", "CWE-434", "CWE-190", "CWE-476", "CWE-502", "CWE-306",
        "CWE-798", "CWE-862", "CWE-276", "CWE-94", "CWE-611", "CWE-863",
        "CWE-732", "CWE-829", "CWE-327", "CWE-200"
    }
    
    # Find which Top 25 CWEs were actually detected
    detected_cwes = set(df_consolidated['CWE_ID_Normalized'].unique())
    detected_top25 = sorted([cwe for cwe in detected_cwes if cwe in TOP_25_CWE])
    
    if not detected_top25:
        print("⚠️ No Top 25 CWEs detected, skipping heatmap")
        return
    
    # Create heatmap matrix
    heatmap_data = []
    for tool in tools:
        row = []
        for cwe in detected_top25:
            tool_cwe_data = df_consolidated[(df_consolidated['Tool_name'] == tool) & 
                                          (df_consolidated['CWE_ID_Normalized'] == cwe)]
            if not tool_cwe_data.empty:
                findings_count = tool_cwe_data['Number_of_Findings'].sum()
                # Use log scale for better visualization of varying magnitudes
                row.append(np.log10(findings_count + 1))  # +1 to avoid log(0)
            else:
                row.append(0)
        heatmap_data.append(row)
    
    # Create DataFrame for heatmap
    heatmap_df = pd.DataFrame(heatmap_data, index=tools, columns=detected_top25)
    
    # Create the heatmap
    plt.figure(figsize=(max(12, len(detected_top25) * 0.8), 8))
    
    # Create heatmap with custom colormap
    mask = heatmap_df == 0  # Mask zeros for better visualization
    
    sns.heatmap(heatmap_df, 
                annot=True, 
                fmt='.1f',
                cmap='YlOrRd',
                mask=None,  # Show all values including zeros
                cbar_kws={'label': 'Log10(Findings + 1)'},
                linewidths=0.5,
                square=False)
    
    plt.title('Top 25 CWE Detection Heatmap by Security Tool\n(Color intensity = Log scale of findings count)', 
              fontweight='bold', fontsize=14, pad=20)
    plt.xlabel('Top 25 CWE IDs Detected', fontsize=12)
    plt.ylabel('Security Tools', fontsize=12)
    
    # Rotate x-axis labels for better readability
    plt.xticks(rotation=45, ha='right')
    plt.yticks(rotation=0)
    
    plt.tight_layout()
    plt.savefig('plot4_cwe_heatmap.png', dpi=300, bbox_inches='tight')
    plt.show()

def create_coverage_gaps_plot():
    """Create a separate plot showing coverage gaps"""
    
    # Standard Top 25 list
    standard_top25 = [
        "CWE-79", "CWE-89", "CWE-787", "CWE-20", "CWE-125", "CWE-78", "CWE-416",
        "CWE-22", "CWE-352", "CWE-434", "CWE-190", "CWE-476", "CWE-502", "CWE-306",
        "CWE-798", "CWE-862", "CWE-276", "CWE-94", "CWE-611", "CWE-863",
        "CWE-732", "CWE-829", "CWE-327", "CWE-200"
    ]
    
    # Load detection matrix to see what's covered
    matrix_df = pd.read_csv('cwe_detection_matrix.csv')
    detected_top25 = matrix_df[matrix_df['Is_Top_25'] == True]['CWE_ID'].tolist()
    
    # Categorize CWEs
    covered_cwes = [cwe for cwe in standard_top25 if cwe in detected_top25]
    missing_cwes = [cwe for cwe in standard_top25 if cwe not in detected_top25]
    
    # Create the plot
    plt.figure(figsize=(14, 8))
    
    # Create data for the plot
    categories = ['Covered by Tools', 'Coverage Gaps']
    counts = [len(covered_cwes), len(missing_cwes)]
    colors_gap = ['#2ECC71', '#E74C3C']  # Green for covered, Red for gaps
    
    # Create bar chart
    bars = plt.bar(categories, counts, color=colors_gap, alpha=0.8, edgecolor='black', linewidth=2)
    
    # Add count labels
    for bar, count in zip(bars, counts):
        plt.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.1, 
                f'{count}/25\n({count/25*100:.1f}%)', 
                ha='center', va='bottom', fontweight='bold', fontsize=14)
    
    plt.title('Top 25 CWE Coverage vs Gaps Analysis', fontweight='bold', fontsize=16, pad=20)
    plt.ylabel('Number of CWEs', fontsize=12)
    plt.ylim(0, max(counts) * 1.2)
    
    # Add text annotations showing specific CWEs
    plt.figtext(0.15, 0.02, f"Covered CWEs:\n{', '.join(covered_cwes[:8])}\n{', '.join(covered_cwes[8:])}", 
                fontsize=9, bbox=dict(boxstyle='round', facecolor='lightgreen', alpha=0.3))
    
    plt.figtext(0.55, 0.02, f"Missing CWEs:\n{', '.join(missing_cwes[:8])}\n{', '.join(missing_cwes[8:])}", 
                fontsize=9, bbox=dict(boxstyle='round', facecolor='lightcoral', alpha=0.3))
    
    plt.grid(axis='y', alpha=0.3, linestyle='--')
    plt.tight_layout()
    plt.subplots_adjust(bottom=0.25)  # Make room for annotations
    plt.savefig('plot5_coverage_gaps.png', dpi=300, bbox_inches='tight')
    plt.show()

def analyze_tool_specializations():
    """Analyze what each tool specializes in"""
    
    print(f"\n🔬 TOOL SPECIALIZATION ANALYSIS:")
    print("-" * 40)
    
    # Load detection matrix
    matrix_df = pd.read_csv('cwe_detection_matrix.csv')
    
    # Analyze each tool's unique strengths
    tools = ['bandit', 'codeql', 'semgrep']
    
    for tool in tools:
        detected_col = f'{tool}_Detected'
        findings_col = f'{tool}_Findings'
        
        # Get CWEs only this tool found
        tool_unique = matrix_df[matrix_df[detected_col] == True]
        other_tools = [t for t in tools if t != tool]
        
        for other_tool in other_tools:
            other_detected_col = f'{other_tool}_Detected'
            tool_unique = tool_unique[tool_unique[other_detected_col] == False]
        
        print(f"\n🔧 {tool.upper()} Specializations:")
        
        if not tool_unique.empty:
            unique_cwes = tool_unique['CWE_ID'].tolist()
            unique_top25 = tool_unique[tool_unique['Is_Top_25'] == True]['CWE_ID'].tolist()
            
            print(f"   • Unique CWEs (only {tool} found): {len(unique_cwes)}")
            if unique_cwes:
                print(f"     {', '.join(unique_cwes)}")
            
            if unique_top25:
                print(f"   • Unique Top 25 CWEs: {', '.join(unique_top25)}")
            
            # Top findings for this tool
            top_findings = matrix_df[matrix_df[detected_col] == True].nlargest(3, findings_col)
            if not top_findings.empty:
                print(f"   • Highest volume findings:")
                for _, row in top_findings.iterrows():
                    marker = "⭐" if row['Is_Top_25'] else "•"
                    print(f"     {marker} {row['CWE_ID']}: {row[findings_col]} findings")
        else:
            print(f"   • No unique CWEs (all findings overlap with other tools)")
    
    # Overall coverage gaps
    print(f"\n❌ COVERAGE GAPS (Top 25 CWEs NOT detected by any tool):")
    print("-" * 55)
    
    top25_in_data = matrix_df[matrix_df['Is_Top_25'] == True]['CWE_ID'].tolist()
    
    # Standard Top 25 list
    standard_top25 = [
        "CWE-79", "CWE-89", "CWE-787", "CWE-20", "CWE-125", "CWE-78", "CWE-416",
        "CWE-22", "CWE-352", "CWE-434", "CWE-190", "CWE-476", "CWE-502", "CWE-306",
        "CWE-798", "CWE-862", "CWE-276", "CWE-94", "CWE-611", "CWE-863",
        "CWE-732", "CWE-829", "CWE-327", "CWE-200"
    ]
    
    missing_cwes = [cwe for cwe in standard_top25 if cwe not in top25_in_data]
    
    if missing_cwes:
        print(f"Missing CWEs ({len(missing_cwes)}/25): {', '.join(missing_cwes)}")
    else:
        print("✅ All Top 25 CWEs covered by at least one tool!")

def main():
    """Main function to run all analyses"""
    try:
        create_summary_report()
        analyze_tool_specializations()
        create_key_visualizations()
        
        print(f"\n🎉 Complete CWE coverage analysis finished!")
        print(f"📁 Generated files:")
        print(f"   • cwe_coverage_summary.png - Key visualizations")
        print(f"   • tool_coverage_summary.csv - Metrics summary")
        print(f"   • cwe_detection_matrix.csv - Detailed detection matrix")
        
    except FileNotFoundError as e:
        print(f"❌ Error: Required file not found - {e}")
    except Exception as e:
        print(f"❌ Error during analysis: {e}")

if __name__ == "__main__":
    main()