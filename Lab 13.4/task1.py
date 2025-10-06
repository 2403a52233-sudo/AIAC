"""
Task 1: Refactor repeated loops into a cleaner, more Pythonic approach.
Refactored legacy code using list comprehension instead of explicit loops.
"""

# Refactored using list comprehension
numbers = [1, 2, 3, 4, 5]
squares = [n ** 2 for n in numbers]
print(squares)
