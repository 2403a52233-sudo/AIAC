def calculate_grade(score: int) -> str:
    """
    Calculate letter grade based on numerical score using elif logic.
    
    Args:
        score: The numerical score (0-100)
    
    Returns:
        Letter grade (A, B, C, D, or F)
    """
    # Cleaner logic using elif instead of nested if-else
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"

# Test the function
test_scores = [95, 85, 75, 65, 55]

print("Grade calculation using elif logic:")
for score in test_scores:
    grade_result = calculate_grade(score)
    print(f"Score {score}: Grade {grade_result}")
