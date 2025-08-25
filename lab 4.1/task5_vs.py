import string
from collections import Counter

def most_frequent_word(paragraph):
    # Convert to lowercase
    paragraph = paragraph.lower()
    # Remove punctuation
    paragraph = paragraph.translate(str.maketrans('', '', string.punctuation))
    # Tokenization
    words = paragraph.split()
    # Count word frequency
    freq = Counter(words)
    # Find the most frequent word
    most_common = freq.most_common(1)
    return most_common[0][0] if most_common else None

# Example usage
paragraph = input("Enter a paragraph: ")
print(most_frequent_word(paragraph))