import openpyxl

wb = openpyxl.Workbook()
ws = wb.active

# Excel currency format pattern matching the image spacing
excel_number_pattern = '"$"\\ #,##0.00'

rows = [
    ["ខែ", "ប្រាក់ចំណូល"],
    ["មករា", 1000.0],
    ["កុម្ភៈ", 2000.0],
    ["មីនា", 3000.0],
    ["មេសា", 6400.0],
]

for row in rows:
    ws.append(row)

# Apply formatting pattern to column B (skipping header)
for cell in ws["B"][1:]:
    cell.number_format = excel_number_pattern

wb.save("pattern_output.xlsx")