import csv
def analyze_csv_file(filepath):
    """
    Analyze a CSV file and return:
    - Number of rows
    - Number of completely empty rows
    - Total word count in all cells
    """
    num_rows = 0
    num_empty_rows = 0
    total_words = 0
    with open(filepath, encoding='utf-8', newline='') as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            num_rows += 1
            if not any(cell.strip() for cell in row):
                num_empty_rows += 1
            else:
                total_words += sum(len(cell.split()) for cell in row if cell.strip())
    return num_rows, num_empty_rows, total_words
csv_content = [
    ["hello ", "this is test"],
    ["", ""],
    ["a ", "d e"]]
csv_filename = "example.csv"
with open(csv_filename, "w", encoding="utf-8", newline='') as f:
    writer = csv.writer(f)
    writer.writerows(csv_content)
rows, empty_rows, words = analyze_csv_file(csv_filename)
print(f"Rows: {rows}")
print(f"Empty rows: {empty_rows}")
print(f"Total words: {words}")