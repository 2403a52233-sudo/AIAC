def determine_age_category(user_age):
   
    match user_age:
        case age if age < 0:
            return "Invalid age"
        case age if 0 <= age <= 12:
            return "Child"
        case age if 13 <= age <= 19:
            return "Teen"
        case age if 20 <= age <= 59:
            return "Adult"
        case _:
            return "Senior"

if __name__ == "__main__":
    user_age = int(input("Enter age: "))
    result = determine_age_category(user_age)
    print(f"Age group: {result}")