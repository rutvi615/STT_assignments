import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load merged dataset
df = pd.read_csv("commit_with_similarity.csv")  
# (make sure this file has MI, CC, LOC, Semantic_Similarity, Token_Similarity, and classifications)

# === Part (b): Descriptive Stats ===
plt.figure()
df['LLM Inference (fix type)'].value_counts().plot(kind='bar')
plt.title("Distribution of Fix Types")
plt.savefig("fix_type_distribution.png")

plt.figure()
df['File Extension'] = df['File Name'].str.split('.').str[-1]
df['File Extension'].value_counts().head(10).plot(kind='bar')
plt.title("Most Modified File Extensions")
plt.savefig("file_extensions.png")

# === Part (c): Structural Metrics ===
metrics = ['MI', 'CC', 'LOC']
for m in metrics:
    plt.figure()
    sns.boxplot(data=df[[f"{m}_Before", f"{m}_After"]])
    plt.title(f"{m} Before vs After")
    plt.savefig(f"{m.lower()}_before_after.png")

    plt.figure()
    sns.histplot(df[f"{m}_Change"], kde=True)
    plt.title(f"Distribution of {m} Change")
    plt.savefig(f"{m.lower()}_change.png")

# === Part (d): Similarity Metrics ===
plt.figure()
sns.histplot(df['Semantic_Similarity'], bins=20, kde=True)
plt.title("Semantic Similarity Distribution")
plt.savefig("semantic_similarity.png")

plt.figure()
sns.histplot(df['Token_Similarity'], bins=20, kde=True)
plt.title("Token Similarity Distribution")
plt.savefig("token_similarity.png")

plt.figure()
sns.scatterplot(x='Semantic_Similarity', y='Token_Similarity', data=df)
plt.title("Semantic vs Token Similarity")
plt.savefig("similarity_scatter.png")

# === Part (e): Classification ===
plt.figure()
df['Semantic_Class'].value_counts().plot(kind='bar')
plt.title("Semantic Classification (Major vs Minor)")
plt.savefig("semantic_classification.png")

plt.figure()
df['Token_Class'].value_counts().plot(kind='bar')
plt.title("Token Classification (Major vs Minor)")
plt.savefig("token_classification.png")

# Agreement Heatmap
plt.figure()
agreement = pd.crosstab(df['Semantic_Class'], df['Token_Class'])
sns.heatmap(agreement, annot=True, fmt="d", cmap="Blues")
plt.title("Agreement Between Semantic & Token Classification")
plt.savefig("agreement_heatmap.png")

print("All plots saved!")
