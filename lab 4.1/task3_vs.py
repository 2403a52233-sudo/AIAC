# task3_vs.py

def get_student_info():
    student = {
        "name": {
            "first": input("first name: "),
            "last": input("Last name: ")
        },
        "branch": input("Branch: "),
        "sgpa": input("SGPA:")
    }
    print("student information:")
    print(f"Full name: {student['name']['first']} {student['name']['last']}")
    print(f"Branch: {student['branch']}")
    print(f"SGPA:{student['sgpa']}")

if __name__ == "__main__":
    get_student_info()
