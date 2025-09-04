# rectify_commit_msg.py
# Adds a 'Rectified Message' column to commit_predictions.csv using a simple rectifier formulation.

import pandas as pd
import os
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
import torch


def sum_diff(diff_path, max_lines=6):
	if diff_path and os.path.exists(diff_path):
		with open(diff_path, "r", encoding="utf-8") as f:
			lines = f.readlines()
			summary = " ".join([line.strip() for line in lines[:max_lines]])
			return summary
	return ""

def sum_code(code_path, max_lines=6):
	if code_path and os.path.exists(code_path):
		with open(code_path, "r", encoding="utf-8") as f:
			lines = f.readlines()
			summary = " ".join([line.strip() for line in lines[:max_lines]])
			return summary
	return ""


def rectifier(commit_msg, fix_type, diff_path, file_name, before_path, after_path):
	"""
	Rectify the commit message using LLM-based logic with more context.
	"""
	MODEL_NAME = "mamiksik/CommitPredictorT5"
	if not hasattr(rectifier, "tokenizer"):
		rectifier.tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
		rectifier.model = AutoModelForSeq2SeqLM.from_pretrained(MODEL_NAME)
	tokenizer = rectifier.tokenizer
	model = rectifier.model

	diff_summary = sum_diff(diff_path)
	before_summary = sum_code(before_path)
	after_summary = sum_code(after_path)

	input_text = (
		f"rectify: Commit message: {commit_msg.strip()} | "
		f"Fix type: {fix_type} | "
		f"File: {file_name} | "
		f"Diff summary: {diff_summary} | "
		f"Before: {before_summary} | "
		f"After: {after_summary}"
	)
	inputs = tokenizer(input_text, return_tensors="pt", truncation=True, max_length=512)
	with torch.no_grad():
		outputs = model.generate(**inputs, max_length=64)
	rectified = tokenizer.decode(outputs[0], skip_special_tokens=True)
	return rectified

csv_p = "commit_predictions.csv"
df = pd.read_csv(csv_p)

# Add the Rectified Message column
df["Rectified Message"] = df.apply(
	lambda row: rectifier(
		row["Commit Message"],
		row["LLM Inference (fix type)"],
		row["Diff File Path"],
		row["File Name"],
		row["Source Code Before File Path"],
		row["Source Code After File Path"]
	),
	axis=1
)

df.to_csv(csv_p, index=False)
print("Rectified Message column added to commit_predictions.csv")