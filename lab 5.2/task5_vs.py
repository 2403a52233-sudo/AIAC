def greet_user(name, gender):
    if gender.lower() == "male":
        title = "Mr."
    elif gender.lower() == "female":
        title = "Ms."
    else:
        # Gender-neutral option
        title = "Mx."

    return f"Hello, {title} {name}! Welcome."


# --- User Input Section ---
name = input("Enter your name: ")
gender = input("Enter your gender (male/female/neutral): ")

print(greet_user(name, gender))