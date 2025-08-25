import csv, re, os

def analyze_csv_data(reader):
    rows, empty, words = 0, 0, 0
    for row in reader:
        rows += 1
        cells = [str(c or '').strip() for c in row]
        if not cells or all(c == "" for c in cells): empty += 1
        words += sum(len(re.findall(r"\b\w+\b", cell)) for cell in cells)
    return rows, empty, words

def main():
    inp = input("Enter CSV file path or CSV text (Enter for default 'data.csv'): ").strip()
    try:
        if not inp or os.path.exists(inp):
            with open(inp or "data.csv", encoding="utf-8") as f:
                reader = csv.reader(f)
                rows, empty, words = analyze_csv_data(reader)
        else:
            reader = csv.reader(inp.splitlines())
            rows, empty, words = analyze_csv_data(reader)
        print(f"Total rows: {rows}\nEmpty rows: {empty}\nTotal words: {words}")
    except FileNotFoundError:
        print("Error: File not found.")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()