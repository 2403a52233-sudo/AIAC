"""
Optimize nested loops for searching.

Refactored legacy loop-based search using Python's 'in' keyword for efficiency.
Legacy code used manual loop with flag variable and break statement to find
elements. The refactored solution uses the 'in' operator which is optimized
at the C level and provides cleaner, more Pythonic code.
"""

# Refactored using 'in' keyword
items = [10, 20, 30, 40, 50]
result = "Found" if 30 in items else "Not Found"
print(result)
