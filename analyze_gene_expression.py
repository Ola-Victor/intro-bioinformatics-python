# Gene Expression Analysis using pandas

import pandas as pd

# Load the CSV file
data = pd.read_csv("gene_expression2.csv", encoding="latin-1")

print("Gene Expression Data:")
print(data)

# Basic analysis
average_expression = data["Expression_Level"].mean()
max_expression = data["Expression_Level"].max()
min_expression = data["Expression_Level"].min()

print("\nSummary Statistics:")
print("Average Expression:", average_expression)
print("Maximum Expression:", max_expression)
print("Minimum Expression:", min_expression)