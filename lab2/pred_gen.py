import csv
import os
import torch
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

# Load tokenizer and model
MODEL_NAME = "mamiksik/CommitPredictorT5"
tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
model = AutoModelForSeq2SeqLM.from_pretrained(MODEL_NAME)

def classify_fix_type(diff_content: str) -> str:
    """
    Use the pre-trained model to predict the type of fix
    from a given diff text.
    """
    prompt = f"commit: {diff_content}"
    encoded = tokenizer(prompt, return_tensors="pt", truncation=True, max_length=512)
    with torch.no_grad():
        output = model.generate(**encoded, max_length=32)
    return tokenizer.decode(output[0], skip_special_tokens=True)

# Input and output CSV paths
input_csv = "commit_diffs.csv"
output_csv = "commit_predictions.csv"
diff_column = "Diff File Path"

# Process CSV rows
with open(input_csv, "r", encoding="utf-8") as infile, \
     open(output_csv, "w", encoding="utf-8", newline="") as outfile:

    reader = csv.DictReader(infile)
    fieldnames = reader.fieldnames + ["LLM Inference (fix type)"]
    writer = csv.DictWriter(outfile, fieldnames=fieldnames, quoting=csv.QUOTE_ALL)

    writer.writeheader()

    for row in reader:
        diff_file_path = row.get(diff_column, "")
        prediction = ""

        if diff_file_path and os.path.exists(diff_file_path):
            with open(diff_file_path, "r", encoding="utf-8") as diff_file:
                diff_data = diff_file.read().strip()
                if diff_data:
                    prediction = classify_fix_type(diff_data)

        row["LLM Inference (fix type)"] = prediction
        writer.writerow(row)

print(f"Predictions saved to {output_csv}")
