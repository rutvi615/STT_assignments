import pandas as pd
import torch
from transformers import AutoTokenizer, AutoModel
from nltk.translate.bleu_score import sentence_bleu, SmoothingFunction

# Load dataset
print("Loading dataset: commit_with_metrics.csv")
df = pd.read_csv("commit_with_metrics.csv")

# Load CodeBERT model for semantic similarity
print("Loading CodeBERT model...")
tokenizer = AutoTokenizer.from_pretrained("microsoft/codebert-base")
model = AutoModel.from_pretrained("microsoft/codebert-base")

def get_codebert_embedding(text):
    """Convert source code into embedding vector using CodeBERT"""
    if pd.isna(text) or str(text).strip() == "":
        return torch.zeros(768)  # empty vector for missing code
    inputs = tokenizer(text, return_tensors="pt", truncation=True, padding=True, max_length=512)
    with torch.no_grad():
        outputs = model(**inputs)
        embeddings = outputs.last_hidden_state.mean(dim=1).squeeze()
    return embeddings

def cosine_similarity(vec1, vec2):
    """Cosine similarity between two torch vectors"""
    if vec1.norm().item() == 0 or vec2.norm().item() == 0:
        return 0.0
    return torch.nn.functional.cosine_similarity(vec1.unsqueeze(0), vec2.unsqueeze(0)).item()

def compute_semantic_similarity(code_before, code_after):
    emb1 = get_codebert_embedding(str(code_before))
    emb2 = get_codebert_embedding(str(code_after))
    return cosine_similarity(emb1, emb2)

# BLEU for token similarity
smooth_fn = SmoothingFunction().method1

def compute_bleu(code_before, code_after):
    if pd.isna(code_before) or pd.isna(code_after):
        return 0.0
    ref_tokens = str(code_before).split()
    hyp_tokens = str(code_after).split()
    if len(ref_tokens) == 0 or len(hyp_tokens) == 0:
        return 0.0
    return sentence_bleu([ref_tokens], hyp_tokens, smoothing_function=smooth_fn)

print("Computing Semantic & Token similarities... (this may take time)")

semantic_scores = []
token_scores = []

for idx, row in df.iterrows():
    sem_sim = compute_semantic_similarity(row["Source Code Before"], row["Source Code After"])
    tok_sim = compute_bleu(row["Source Code Before"], row["Source Code After"])
    semantic_scores.append(sem_sim)
    token_scores.append(tok_sim)

df["Semantic_Similarity"] = semantic_scores
df["Token_Similarity"] = token_scores

# Classification thresholds
SEM_THRESHOLD = 0.8
TOK_THRESHOLD = 0.75

df["Semantic_Class"] = df["Semantic_Similarity"].apply(lambda x: "Minor Fix" if x >= SEM_THRESHOLD else "Major Fix")
df["Token_Class"] = df["Token_Similarity"].apply(lambda x: "Minor Fix" if x >= TOK_THRESHOLD else "Major Fix")

# Save with metrics
output_file = "commit_with_similarity.csv"
df.to_csv(output_file, index=False)
print(f"Saved results with similarity metrics to {output_file}")

print("\n Similarity & Classification Report")
print("-" * 50)

# Semantic classification stats
sem_counts = df["Semantic_Class"].value_counts()
print("Semantic classification:")
print(sem_counts.to_string(), "\n")

# Token classification stats
tok_counts = df["Token_Class"].value_counts()
print("Token classification:")
print(tok_counts.to_string(), "\n")

# Agreement between methods
agreement = (df["Semantic_Class"] == df["Token_Class"]).sum()
total = len(df)
agreement_pct = (agreement / total) * 100 if total > 0 else 0

print(f"Agreement between Semantic & Token classification: {agreement}/{total} ({agreement_pct:.2f}%)")
import matplotlib.pyplot as plt


plt.figure(figsize=(6, 4))
df["Semantic_Class"].value_counts().plot(kind="bar")
plt.title("Semantic Classification Distribution")
plt.xlabel("Class")
plt.ylabel("Number of Commits")
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()


plt.figure(figsize=(6, 4))
df["Token_Class"].value_counts().plot(kind="bar", color="orange")
plt.title("Token Classification Distribution")
plt.xlabel("Class")
plt.ylabel("Number of Commits")
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()


df["Classes_Agree"] = df.apply(
    lambda row: "YES" if row["Semantic_Class"] == row["Token_Class"] else "NO", axis=1
)

plt.figure(figsize=(5, 5))
df["Classes_Agree"].value_counts().plot(
    kind="pie", autopct="%1.1f%%", startangle=90, colors=["#4CAF50", "#F44336"]
)
plt.ylabel("")
plt.title("Agreement Between Semantic & Token Classifications")
plt.tight_layout()
plt.show()
# Pie chart for classification agreement
agreement_counts = df["Classes_Agree"].value_counts()

plt.figure(figsize=(6, 6))
plt.pie(
    agreement_counts,
    labels=agreement_counts.index,
    autopct="%1.1f%%",
    startangle=90,
    colors=["#4CAF50", "#F44336"]
)
plt.title("Semantic vs Token Classification Agreement")
plt.tight_layout()
plt.show()