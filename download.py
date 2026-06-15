# download.py
import pandas as pd
from datasets import load_dataset

print("Downloading the pre-cleaned 'better-cuad' dataset from Hugging Face...")

# Pulling the optimized JSON/Text version instead of the raw PDF container
dataset = load_dataset("umarbutler/better-cuad", split="train")

# Convert directly to a normal Pandas DataFrame
df = pd.DataFrame(dataset)

print(f"\nSuccess! Successfully loaded {len(df)} contract entries.")
print("\nAvailable columns for structuring your training pairs:")
print(df.columns.tolist()[:10])  # Show the first 10 columns for inspection

# Save a 5-row sample to a CSV so you can visually open it up
df.head(5).to_csv("contract_sample.csv", index=False)
print("\nSaved a 5-row sample to 'contract_sample.csv'!")