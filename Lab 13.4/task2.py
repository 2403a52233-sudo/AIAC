"""
Task 2: Simplify string concatenation.

Refactored legacy += concatenation using " ".join() for better efficiency.
Legacy code used loops with += operations which create new string objects
each iteration. The refactored solution uses join() method for optimal
performance and cleaner, more Pythonic code.
"""

# Refactored using " ".join()
words = ["AI", "helps", "in", "refactoring", "code"]
sentence = " ".join(words)
print(sentence)
