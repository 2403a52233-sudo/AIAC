"""
Replace manual dictionary lookup with a safer method.

Refactored legacy dictionary access using .get() method for safer key handling.
Legacy code used manual if-else checks with 'in' operator and direct key access.
The refactored solution uses .get() method which handles missing keys gracefully
and provides a default value, making the code more concise and Pythonic.
"""

# Refactored using .get() method
student_scores = {"Alice": 85, "Bob": 90}
result = student_scores.get("Charlie", "Not Found")
print(result)
