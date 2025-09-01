def classify_age(age):
    match age:
        case age if age < 0:
            return "Invalid age"
        case age if age <= 12:
            return "Child"
        case age if age <= 19:
            return "Teen"
        case age if age <= 59:
            return "Adult"
        case _:
            return "Senior"

if __name__ == "__main__":
    age = int(input("Enter age: "))
    print(f"Age group: {classify_age(age)}")                
        