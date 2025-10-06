class Student:
    """
    A class to represent a student with their personal details and marks.
    Attributes:
        name (str): The student's full name
        age (int): The student's age
        marks (list): List of marks for different subjects
    """
    def __init__(self, name, age, *marks):
        """
        Initialize a Student object.  
        Args:
            name (str): The student's full name
            age (int): The student's age
            *marks: Variable number of marks (0-100 each)
        """
        self.name = name
        self.age = age
        self.marks = list(marks)
    def details(self):
        """
        Print the student's name and age with improved formatting.
        """
        print(f"Student Details:")
        print(f"  Name: {self.name}")
        print(f"  Age: {self.age}")
    def total(self):
        """
        Calculate the total marks across all subjects using sum().
        Returns:
            int: The sum of all marks
        """
        return sum(self.marks)
    def average(self):
        """
        Calculate the average marks across all subjects.
        Returns:
            float: The average of all marks
        """
        return sum(self.marks) / len(self.marks) if self.marks else 0
# Example usage
if __name__ == "__main__":
    student = Student("John Doe", 20, 85, 92, 78)
    student.details()
    print(f"Total marks: {student.total()}")
    print(f"Average marks: {student.average():.2f}")
    print(f"Individual marks: {student.marks}")
