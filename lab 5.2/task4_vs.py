def applicant_score(education, experience, gender, age):
    score = 0

    # Education scoring
    if education == "PhD":
        score += 30
    elif education == "Masters":
        score += 20
    elif education == "Bachelors":
        score += 10
    else:
        score += 5

    # Experience scoring
    if experience >= 10:
        score += 40
    elif experience >= 5:
        score += 25
    else:
        score += 10

    # Gender scoring (⚠️ Potential bias)
    if gender.lower() == "male":
        score += 10
    elif gender.lower() == "female":
        score += 5
    else:
        score += 0

    # Age scoring
    if 25 <= age <= 40:
        score += 20
    else:
        score += 10

    return score


# Example usage
print("John:", applicant_score("Masters", 7, "male", 30))
print("Priya:", applicant_score("Masters", 7, "female", 30))
