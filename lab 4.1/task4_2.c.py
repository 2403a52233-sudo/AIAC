import csv
import sys
def analyze_csv(filename):
    """
    Read a .csv file and return:
    - total number of rows
    - number of empty rows (all cells blank after strip)
    - total number of words across the file (whitespace-separated)
    """
    total_rows = 0
    empty_rows = 0
    word_count = 0
    with open(filename, newline='', encoding='utf-8') as f:
        reader = csv.reader(f)
        for row in reader:
            total_rows += 1
            stripped = [c.strip() for c in row]
            if len(stripped) == 0 or all(c == '' for c in stripped):
                empty_rows += 1
            else:
                for cell in stripped:
                    if cell:
                        word_count += len(cell.split())
    return total_rows, empty_rows, word_count
def main():
    if len(sys.argv) > 1:
        path = sys.argv[1]
        total_rows, empty_rows, word_count = analyze_csv(path)
        print(f"Total rows in file   : {total_rows}")
        print(f"Number of empty rows : {empty_rows}")
        print(f"Total words in file  : {word_count}")
        return
    sample_csv = """hello world, this is test
, 
a b c, d e
"""
    sample_path = 'sample.csv'
    with open(sample_path, 'w', encoding='utf-8', newline='') as f:
        f.write(sample_csv)

    total_rows, empty_rows, word_count = analyze_csv(sample_path)
    print(f"Total rows in file   : {total_rows}")
    print(f"Number of empty rows : {empty_rows}")
    print(f"Total words in file  : {word_count}")
if __name__ == '__main__':
    main()


