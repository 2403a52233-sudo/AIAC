import csv
def analyze_csv(filename):
    """
    Reads a CSV file and returns:
    - Total number of rows
    - Number of empty rows
    - Total number of words across the file
    """
    total_rows = 0
    empty_rows = 0
    word_count = 0

    with open(filename, newline='', encoding="utf-8") as f:
        reader = csv.reader(f)
        for row in reader:
            total_rows += 1
            # Check if entire row is empty
            if all(cell.strip() == "" for cell in row):
                empty_rows += 1
            else:
                # Count words in non-empty cells
                for cell in row:
                    word_count += len(cell.split())

    return total_rows, empty_rows, word_count
sample_csv = """hello world,this is test
,
a b c,d e
"""

filename = "sample.csv"
with open(filename, "w", encoding="utf-8") as f:
    f.write(sample_csv)

result = analyze_csv(filename)
print("Total rows:", result[0])
print("Empty rows:", result[1])
print("Total words:", result[2])
