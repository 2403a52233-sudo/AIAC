import csv
import re
import os
WORD_REGEX = re.compile(r"\b\w+\b", re.UNICODE)
def count_words_in_cells(cells):
    total = 0
    for cell in cells:
        if cell is None:
            continue
        total += len(WORD_REGEX.findall(str(cell)))
    return total
def analyze_csv(file_path):
    total_rows = 0
    empty_rows = 0
    total_words = 0
    with open(file_path, mode="r", encoding="utf-8", newline="") as f:
        reader = csv.reader(f)
        for row in reader:
            total_rows += 1
            cells = ["" if c is None else str(c).strip() for c in row]
            if len(cells) == 0 or all(c == "" for c in cells):
                empty_rows += 1
            total_words += count_words_in_cells(cells)
    return total_rows, empty_rows, total_words
def analyze_csv_from_text(text):
    total_rows = 0
    empty_rows = 0
    total_words = 0
    lines = text.splitlines() if "\n" in text else [text]
    reader = csv.reader(lines)
    for row in reader:
        total_rows += 1
        cells = ["" if c is None else str(c).strip() for c in row]
        if len(cells) == 0 or all(c == "" for c in cells):
            empty_rows += 1
        total_words += count_words_in_cells(cells)
    return total_rows, empty_rows, total_words
def main():
    try:
        user_input = input("Enter CSV file path or CSV text (Enter for default 'data.csv'): ").strip()

        if not user_input:
            total_rows, empty_rows, total_words = analyze_csv("data.csv")
        elif os.path.exists(user_input):
            total_rows, empty_rows, total_words = analyze_csv(user_input)
        else:
            total_rows, empty_rows, total_words = analyze_csv_from_text(user_input)

        print(f"Total rows in file   : {total_rows}")
        print(f"Number of empty rows : {empty_rows}")
        print(f"Total words in file  : {total_words}")
    except FileNotFoundError:
        print("Error: File not found. Please check the path and try again.")
    except Exception as e:
        print(f"Error: {e}")
if __name__ == "__main__":
    main()


