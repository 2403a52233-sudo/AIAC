class Student:
    def __init__(self, name, rollno, marks):
        self.name = name
        self.rollno = rollno
        self.marks = marks

    def display(self):
        print(f"Name: {self.name}, Roll No: {self.rollno}, Marks: {self.marks}, Grade: {self.calculate_grade()}")

    def calculate_grade(self):
        if self.marks >= 90:
            return "A"
        elif self.marks >= 75:
            return "B"
        elif self.marks >= 60:
            return "C"
        else:
            return "Fail"

if __name__ == "__main__":
    name = input("Enter student name: ")
    rollno = int(input("Enter roll number: "))
    marks = float(input("Enter marks: "))
    student1 = Student(name, rollno, marks)
    student1.display()