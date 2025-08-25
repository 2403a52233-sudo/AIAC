import re
from collections import Counter

def find_most_frequent_word(paragraph):
    """
    Find the most frequently used word in a paragraph.
    
    Args:
        paragraph (str): Input paragraph text
        
    Returns:
        tuple: (most_frequent_word, frequency_count)
    """

    text_lower = paragraph.lower()
    text_clean = re.sub(r'[^\w\s\']', '', text_lower)
    words = text_clean.split()
    word_counts = Counter(words)
    
    if word_counts:
        most_common_word, frequency = word_counts.most_common(1)[0]
        return most_common_word, frequency
    else:
        return None, 0

def main():
    print("Enter a paragraph:")
    paragraph = input()
    
    if not paragraph.strip():
        print("No text entered.")
        return
    
    most_frequent_word, frequency = find_most_frequent_word(paragraph)
    
    if most_frequent_word:
        print(f"Most frequent word: {most_frequent_word}")
    else:
        print("No words found in the text.")

if __name__ == "__main__":
    main()
