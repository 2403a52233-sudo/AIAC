"""
Refactor repetitive if-else blocks.

Refactored legacy if-elif-else chain using dictionary mapping for cleaner code.
Legacy code used multiple conditional statements for different operations.
The refactored solution uses a dictionary with lambda functions to map
operations to their corresponding functions, making the code more scalable
and easier to maintain.
"""

# Refactored using dictionary mapping
operation = "multiply"
a, b = 5, 3

operations = {
    "add": lambda x, y: x + y,
    "subtract": lambda x, y: x - y,
    "multiply": lambda x, y: x * y
}

result = operations.get(operation, lambda x, y: None)(a, b)
print(result)
