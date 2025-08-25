import csv, sys

def analyze_csv(filename):
    with open(filename, encoding='utf-8', newline='') as f:
        rows = list(csv.reader(f))
    total = len(rows)
    empty = sum(all(not c.strip() for c in row) for row in rows)
    words = sum(len(c.strip().split()) for row in rows for c in row if c.strip())
    return total, empty, words

if __name__ == '__main__':
    file = sys.argv[1] if len(sys.argv) > 1 else 'sample.csv'
    if file == 'sample.csv':
        with open(file, 'w', encoding='utf-8', newline='') as f:
            f.write("Good morning\n, \to, everyone\n")
    t, e, w = analyze_csv(file)
    print(f"Total rows in file   : {t}")
    print(f"Number of empty rows : {e}")
    print(f"Total words in file  : {w}")