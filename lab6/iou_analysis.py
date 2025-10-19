#!/usr/bin/env python3
"""
Pairwise Agreement (IoU) Analysis for Security Tools
Computes Jaccard Index (Intersection over Union) for tool pairs
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from itertools import combinations
import json

def load_and_prepare_data():
    """Load consolidated findings and prepare CWE sets for each tool"""
    print("📊 Loading consolidated findings for IoU analysis...")
    
    # Load consolidated findings
    df = pd.read_csv('consolidated_findings.csv')
    
    # Normalize CWE IDs to consistent format
    def normalize_cwe_id(cwe_id):
        if str(cwe_id).startswith("CWE-"):
            return str(cwe_id)
        else:
            return f"CWE-{cwe_id}"
    
    df['CWE_ID_Normalized'] = df['CWE_ID'].apply(normalize_cwe_id)
    
    # Get unique tools
    tools = sorted(df['Tool_name'].unique())
    
    # Create CWE sets for each tool
    tool_cwe_sets = {}
    for tool in tools:
        tool_df = df[df['Tool_name'] == tool]
        cwe_set = set(tool_df['CWE_ID_Normalized'].unique())
        tool_cwe_sets[tool] = cwe_set
        print(f"🔧 {tool}: {len(cwe_set)} unique CWEs")
    
    return tools, tool_cwe_sets, df

def compute_jaccard_index(set1, set2):
    """Compute Jaccard Index (IoU) between two sets"""
    if len(set1) == 0 and len(set2) == 0:
        return 1.0  # Both empty sets are considered identical
    
    intersection = len(set1.intersection(set2))
    union = len(set1.union(set2))
    
    if union == 0:
        return 0.0
    
    return intersection / union

def compute_iou_matrix(tools, tool_cwe_sets):
    """Compute the Tool × Tool IoU Matrix"""
    print("\n🔍 Computing pairwise IoU (Jaccard Index) matrix...")
    
    n_tools = len(tools)
    iou_matrix = np.zeros((n_tools, n_tools))
    
    # Detailed pairwise analysis
    pairwise_details = {}
    
    for i, tool1 in enumerate(tools):
        for j, tool2 in enumerate(tools):
            if i == j:
                # Diagonal: tool with itself = 1.0
                iou_matrix[i][j] = 1.0
            else:
                # Compute Jaccard Index
                set1 = tool_cwe_sets[tool1]
                set2 = tool_cwe_sets[tool2]
                
                intersection = set1.intersection(set2)
                union = set1.union(set2)
                
                iou = compute_jaccard_index(set1, set2)
                iou_matrix[i][j] = iou
                
                # Store detailed analysis
                pair_key = f"{tool1}-{tool2}"
                pairwise_details[pair_key] = {
                    'tool1': tool1,
                    'tool2': tool2,
                    'tool1_cwes': len(set1),
                    'tool2_cwes': len(set2),
                    'intersection': list(intersection),
                    'intersection_count': len(intersection),
                    'union_count': len(union),
                    'iou': iou,
                    'tool1_unique': list(set1 - set2),
                    'tool2_unique': list(set2 - set1),
                    'tool1_unique_count': len(set1 - set2),
                    'tool2_unique_count': len(set2 - set1)
                }
    
    return iou_matrix, pairwise_details

def analyze_tool_combinations(tools, tool_cwe_sets):
    """Analyze different tool combinations for maximum CWE coverage"""
    print("\n🎯 Analyzing tool combinations for maximum coverage...")
    
    all_cwes = set()
    for cwe_set in tool_cwe_sets.values():
        all_cwes.update(cwe_set)
    
    total_unique_cwes = len(all_cwes)
    
    combination_analysis = {}
    
    # Single tools
    for tool in tools:
        coverage = len(tool_cwe_sets[tool]) / total_unique_cwes * 100
        combination_analysis[tool] = {
            'tools': [tool],
            'cwes_covered': len(tool_cwe_sets[tool]),
            'coverage_percent': coverage,
            'unique_contribution': len(tool_cwe_sets[tool])
        }
    
    # Pairwise combinations
    for tool1, tool2 in combinations(tools, 2):
        combined_cwes = tool_cwe_sets[tool1].union(tool_cwe_sets[tool2])
        coverage = len(combined_cwes) / total_unique_cwes * 100
        
        # Calculate unique contribution of adding tool2 to tool1
        unique_contribution = len(tool_cwe_sets[tool2] - tool_cwe_sets[tool1])
        
        combination_analysis[f"{tool1}+{tool2}"] = {
            'tools': [tool1, tool2],
            'cwes_covered': len(combined_cwes),
            'coverage_percent': coverage,
            'unique_contribution': unique_contribution,
            'synergy': len(combined_cwes) - len(tool_cwe_sets[tool1]) - len(tool_cwe_sets[tool2]) + len(tool_cwe_sets[tool1].intersection(tool_cwe_sets[tool2]))
        }
    
    # All three tools
    if len(tools) == 3:
        all_combined = set()
        for cwe_set in tool_cwe_sets.values():
            all_combined.update(cwe_set)
        
        coverage = len(all_combined) / total_unique_cwes * 100
        
        combination_analysis["All_Tools"] = {
            'tools': tools,
            'cwes_covered': len(all_combined),
            'coverage_percent': coverage,
            'unique_contribution': 0  # No additional tools to add
        }
    
    return combination_analysis, total_unique_cwes

def create_iou_visualizations(tools, iou_matrix, pairwise_details, combination_analysis):
    """Create comprehensive IoU visualizations"""
    print("\n📈 Creating IoU analysis visualizations...")
    
    # 1. IoU Heatmap
    plt.figure(figsize=(10, 8))
    
    # Create a mask for the upper triangle to show only unique pairs
    mask = np.triu(np.ones_like(iou_matrix, dtype=bool), k=1)
    
    sns.heatmap(iou_matrix, 
                annot=True, 
                fmt='.3f',
                cmap='RdYlBu_r',
                xticklabels=tools,
                yticklabels=tools,
                square=True,
                cbar_kws={'label': 'IoU (Jaccard Index)'},
                linewidths=0.5)
    
    plt.title('Tool × Tool IoU (Jaccard Index) Matrix\nHigher values = More similar CWE detection patterns', 
              fontweight='bold', fontsize=14, pad=20)
    plt.xlabel('Tools', fontsize=12)
    plt.ylabel('Tools', fontsize=12)
    
    plt.tight_layout()
    plt.savefig('plot7_iou_matrix.png', dpi=300, bbox_inches='tight')
    plt.show()
    
    # 2. Pairwise IoU Comparison Bar Chart
    plt.figure(figsize=(12, 7))
    
    # Extract unique pairs (excluding diagonal)
    pair_names = []
    iou_values = []
    
    for i, tool1 in enumerate(tools):
        for j, tool2 in enumerate(tools):
            if i < j:  # Only unique pairs
                pair_names.append(f"{tool1} ∩ {tool2}")
                iou_values.append(iou_matrix[i][j])
    
    colors = ['#FF6B6B', '#4ECDC4', '#45B7D1']
    bars = plt.bar(pair_names, iou_values, color=colors[:len(pair_names)], 
                   alpha=0.8, edgecolor='black', linewidth=1.5)
    
    plt.title('Pairwise Tool Similarity (IoU/Jaccard Index)', fontweight='bold', fontsize=14, pad=20)
    plt.ylabel('IoU (Jaccard Index)', fontsize=12)
    plt.xlabel('Tool Pairs', fontsize=12)
    plt.ylim(0, max(iou_values) * 1.1 if iou_values else 1)
    
    # Add value labels
    for bar, val in zip(bars, iou_values):
        plt.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.01,
                f'{val:.3f}', ha='center', fontweight='bold', fontsize=11)
    
    plt.grid(axis='y', alpha=0.3, linestyle='--')
    plt.tight_layout()
    plt.savefig('plot8_pairwise_iou.png', dpi=300, bbox_inches='tight')
    plt.show()
    
    # 3. Tool Combination Coverage Analysis
    plt.figure(figsize=(12, 8))
    
    # Prepare data for combination analysis
    combo_names = list(combination_analysis.keys())
    coverage_percentages = [combination_analysis[combo]['coverage_percent'] for combo in combo_names]
    cwes_covered = [combination_analysis[combo]['cwes_covered'] for combo in combo_names]
    
    # Sort by coverage percentage
    sorted_data = sorted(zip(combo_names, coverage_percentages, cwes_covered), 
                        key=lambda x: x[1], reverse=True)
    combo_names, coverage_percentages, cwes_covered = zip(*sorted_data)
    
    # Create color gradient
    colors = plt.cm.viridis(np.linspace(0, 1, len(combo_names)))
    
    bars = plt.bar(range(len(combo_names)), coverage_percentages, 
                   color=colors, alpha=0.8, edgecolor='black', linewidth=1.5)
    
    plt.title('CWE Coverage by Tool Combinations', fontweight='bold', fontsize=14, pad=20)
    plt.ylabel('Coverage Percentage (%)', fontsize=12)
    plt.xlabel('Tool Combinations', fontsize=12)
    plt.xticks(range(len(combo_names)), combo_names, rotation=45, ha='right')
    
    # Add dual labels: percentage and absolute count
    for i, (bar, pct, count) in enumerate(zip(bars, coverage_percentages, cwes_covered)):
        plt.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 1,
                f'{pct:.1f}%\n({count} CWEs)', ha='center', fontweight='bold', fontsize=10)
    
    plt.grid(axis='y', alpha=0.3, linestyle='--')
    plt.tight_layout()
    plt.savefig('plot9_combination_coverage.png', dpi=300, bbox_inches='tight')
    plt.show()

def print_detailed_analysis(tools, iou_matrix, pairwise_details, combination_analysis, total_cwes):
    """Print comprehensive analysis results"""
    
    print("\n" + "="*80)
    print("🎯 PAIRWISE AGREEMENT (IoU) ANALYSIS RESULTS")
    print("="*80)
    
    # IoU Matrix Display
    print(f"\n📊 TOOL × TOOL IoU MATRIX:")
    print("-" * 40)
    
    # Create pandas DataFrame for better formatting
    iou_df = pd.DataFrame(iou_matrix, index=tools, columns=tools)
    print(iou_df.round(3))
    
    # Detailed Pairwise Analysis
    print(f"\n🔍 DETAILED PAIRWISE ANALYSIS:")
    print("-" * 50)
    
    for i, tool1 in enumerate(tools):
        for j, tool2 in enumerate(tools):
            if i < j:  # Only unique pairs
                pair_key = f"{tool1}-{tool2}"
                details = pairwise_details[pair_key]
                
                print(f"\n🔧 {tool1.upper()} vs {tool2.upper()}:")
                print(f"   • IoU (Jaccard Index): {details['iou']:.3f}")
                print(f"   • {tool1} CWEs: {details['tool1_cwes']}")
                print(f"   • {tool2} CWEs: {details['tool2_cwes']}")
                print(f"   • Shared CWEs: {details['intersection_count']} ({', '.join(details['intersection'][:5])}{'...' if len(details['intersection']) > 5 else ''})")
                print(f"   • {tool1} unique: {details['tool1_unique_count']} CWEs")
                print(f"   • {tool2} unique: {details['tool2_unique_count']} CWEs")
                print(f"   • Total union: {details['union_count']} CWEs")
    
    # Similarity Interpretation
    print(f"\n📈 SIMILARITY INTERPRETATION:")
    print("-" * 40)
    
    # Find most and least similar pairs
    similarities = []
    for i, tool1 in enumerate(tools):
        for j, tool2 in enumerate(tools):
            if i < j:
                similarities.append((f"{tool1}-{tool2}", iou_matrix[i][j]))
    
    similarities.sort(key=lambda x: x[1], reverse=True)
    most_similar = similarities[0]
    least_similar = similarities[-1]
    
    print(f"🔗 Most Similar Tools: {most_similar[0]} (IoU: {most_similar[1]:.3f})")
    print(f"🔀 Most Diverse Tools: {least_similar[0]} (IoU: {least_similar[1]:.3f})")
    
    # Interpret IoU values
    print(f"\n📋 IoU INTERPRETATION GUIDE:")
    print("   • IoU > 0.7: High similarity (significant overlap)")
    print("   • IoU 0.3-0.7: Moderate similarity (some overlap)")  
    print("   • IoU < 0.3: Low similarity (highly complementary)")
    
    avg_iou = np.mean([sim[1] for sim in similarities])
    print(f"\n📊 Average pairwise IoU: {avg_iou:.3f}")
    
    if avg_iou > 0.7:
        print("   → Tools have HIGH OVERLAP - consider using fewer tools")
    elif avg_iou > 0.3:
        print("   → Tools have MODERATE OVERLAP - good complementary mix")
    else:
        print("   → Tools have LOW OVERLAP - highly complementary suite")
    
    # Coverage Combination Analysis
    print(f"\n🎯 TOOL COMBINATION ANALYSIS:")
    print("-" * 45)
    
    # Sort combinations by coverage
    sorted_combos = sorted(combination_analysis.items(), 
                          key=lambda x: x[1]['coverage_percent'], 
                          reverse=True)
    
    print(f"Total unique CWEs across all tools: {total_cwes}")
    print()
    
    for combo_name, data in sorted_combos:
        tools_str = " + ".join(data['tools'])
        print(f"🔧 {tools_str}:")
        print(f"   • Coverage: {data['coverage_percent']:.1f}% ({data['cwes_covered']}/{total_cwes} CWEs)")
        if 'unique_contribution' in data and len(data['tools']) > 1:
            print(f"   • Incremental value: +{data['unique_contribution']} unique CWEs")
    
    # Strategic Recommendations
    print(f"\n💡 STRATEGIC RECOMMENDATIONS:")
    print("-" * 35)
    
    best_combo = sorted_combos[0]
    print(f"🏆 Maximum Coverage: {best_combo[0]} ({best_combo[1]['coverage_percent']:.1f}%)")
    
    # Find most cost-effective combination
    efficiency_scores = []
    for combo_name, data in combination_analysis.items():
        if len(data['tools']) > 1:
            efficiency = data['coverage_percent'] / len(data['tools'])
            efficiency_scores.append((combo_name, efficiency, data))
    
    if efficiency_scores:
        efficiency_scores.sort(key=lambda x: x[1], reverse=True)
        most_efficient = efficiency_scores[0]
        print(f"⚡ Most Efficient: {most_efficient[0]} ({most_efficient[1]:.1f}% per tool)")
    
    # Coverage gaps and recommendations
    max_coverage = best_combo[1]['coverage_percent']
    if max_coverage < 90:
        print(f"⚠️  Coverage Gap: {100 - max_coverage:.1f}% of potential CWEs not detected")
        print("   → Consider adding additional security tools")
    else:
        print("✅ Excellent coverage achieved with current tool suite")

def export_iou_analysis(tools, iou_matrix, pairwise_details, combination_analysis):
    """Export detailed IoU analysis to files"""
    print(f"\n💾 Exporting IoU analysis results...")
    
    # 1. IoU Matrix CSV
    iou_df = pd.DataFrame(iou_matrix, index=tools, columns=tools)
    iou_df.to_csv('iou_matrix.csv')
    
    # 2. Pairwise details CSV
    pairwise_list = []
    for pair_key, details in pairwise_details.items():
        if details['tool1'] != details['tool2']:  # Exclude diagonal
            pairwise_list.append({
                'Tool_Pair': f"{details['tool1']}-{details['tool2']}",
                'Tool1': details['tool1'],
                'Tool2': details['tool2'],
                'Tool1_CWEs': details['tool1_cwes'],
                'Tool2_CWEs': details['tool2_cwes'],
                'Shared_CWEs': details['intersection_count'],
                'Tool1_Unique': details['tool1_unique_count'],
                'Tool2_Unique': details['tool2_unique_count'],
                'Union_CWEs': details['union_count'],
                'IoU_Jaccard_Index': round(details['iou'], 4),
                'Shared_CWE_List': ', '.join(details['intersection']),
                'Tool1_Unique_List': ', '.join(details['tool1_unique']),
                'Tool2_Unique_List': ', '.join(details['tool2_unique'])
            })
    
    pairwise_df = pd.DataFrame(pairwise_list)
    pairwise_df.to_csv('pairwise_iou_analysis.csv', index=False)
    
    # 3. Combination analysis CSV
    combo_list = []
    for combo_name, data in combination_analysis.items():
        combo_list.append({
            'Combination': combo_name,
            'Tools': ' + '.join(data['tools']),
            'Tool_Count': len(data['tools']),
            'CWEs_Covered': data['cwes_covered'],
            'Coverage_Percent': round(data['coverage_percent'], 2),
            'Unique_Contribution': data.get('unique_contribution', 0),
            'Efficiency_Per_Tool': round(data['coverage_percent'] / len(data['tools']), 2)
        })
    
    combo_df = pd.DataFrame(combo_list)
    combo_df.to_csv('tool_combination_analysis.csv', index=False)
    
    # 4. Complete analysis JSON
    analysis_export = {
        'iou_matrix': iou_matrix.tolist(),
        'tools': tools,
        'pairwise_details': pairwise_details,
        'combination_analysis': combination_analysis,
        'summary_statistics': {
            'average_iou': float(np.mean(iou_matrix[np.triu_indices_from(iou_matrix, k=1)])),
            'max_iou': float(np.max(iou_matrix[np.triu_indices_from(iou_matrix, k=1)])),
            'min_iou': float(np.min(iou_matrix[np.triu_indices_from(iou_matrix, k=1)])),
            'total_unique_cwes': max([data['cwes_covered'] for data in combination_analysis.values()])
        }
    }
    
    with open('iou_analysis_complete.json', 'w') as f:
        json.dump(analysis_export, f, indent=2, default=str)
    
    print("✅ Exported IoU analysis files:")
    print("   📊 iou_matrix.csv - IoU matrix in CSV format")
    print("   🔍 pairwise_iou_analysis.csv - Detailed pairwise analysis")
    print("   📈 tool_combination_analysis.csv - Coverage combination metrics")
    print("   📋 iou_analysis_complete.json - Complete analysis data")

def main():
    """Main function to run IoU analysis"""
    print("🚀 Starting Pairwise Agreement (IoU) Analysis")
    print("="*60)
    
    try:
        # Load and prepare data
        tools, tool_cwe_sets, df = load_and_prepare_data()
        
        # Compute IoU matrix
        iou_matrix, pairwise_details = compute_iou_matrix(tools, tool_cwe_sets)
        
        # Analyze tool combinations
        combination_analysis, total_cwes = analyze_tool_combinations(tools, tool_cwe_sets)
        
        # Create visualizations
        create_iou_visualizations(tools, iou_matrix, pairwise_details, combination_analysis)
        
        # Print detailed analysis
        print_detailed_analysis(tools, iou_matrix, pairwise_details, combination_analysis, total_cwes)
        
        # Export results
        export_iou_analysis(tools, iou_matrix, pairwise_details, combination_analysis)
        
        print(f"\n🎉 Pairwise IoU Analysis Complete!")
        
    except FileNotFoundError:
        print("❌ Error: consolidated_findings.csv not found!")
        print("   Please ensure the CSV file is in the current directory.")
    except Exception as e:
        print(f"❌ Error during IoU analysis: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    main()