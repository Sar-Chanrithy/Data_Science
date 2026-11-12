 import re

text_data = """
ខែ ប្រាក់ចំណូល
មករា $ 1,000.00
កុម្ភៈ $ 2,000.00
មីនា $ 3,000.00
មេសា $ 6,400.00
"""

# Matches: (Khmer text) followed by dollar sign and formatted decimal numbers
pattern = r"([\u1780-\u17FF]+)\s+\$\s*([\d,]+(?:\.\d{2})?)"

results = []
for month, amount in re.findall(pattern, text_data):
    results.append({"ខែ": month, "ប្រាក់ចំណូល": float(amount.replace(",", ""))})

print(results)