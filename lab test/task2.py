class Student:
	"""Represents a student with name, roll number, marks, and derived grade.
	Attributes:
		name (str): Student's full name.
		roll_number (int): Student's roll number.
		marks (float): Marks obtained (0-100 scale).
	"""
	def __init__(self, name: str, roll_number: int, marks: float) -> None:
		if not isinstance(name, str) or not name.strip():
			raise ValueError("name must be a non-empty string")
		if not isinstance(roll_number, int) or roll_number <= 0:
			raise ValueError("roll_number must be a positive integer")
		if not isinstance(marks, (int, float)):
			raise TypeError("marks must be a number")
		if marks < 0 or marks > 100:
			raise ValueError("marks must be between 0 and 100 inclusive")
		self.name: str = name.strip()
		self.roll_number: int = roll_number
		self.marks: float = float(marks)
	def _compute_grade(self) -> str:
		"""Compute letter grade from marks.
		Grading policy:
		- 90–100: A+
		- 75–89 : A
		- 60–74 : B
		- 50–59 : C
		- < 50  : F
		Returns:
			str: Grade as A+, A, B, C, or F.
		"""
		m = self.marks
		if 90 <= m <= 100:
			return "A+"
		elif 75 <= m <= 89:
			return "A"
		elif 60 <= m <= 74:
			return "B"
		elif 50 <= m <= 59:
			return "C"
		return "F"
	def display_details(self) -> None:
		"""Display the student's details: name, roll number, marks, and grade."""
		grade = self._compute_grade()
		print(f"Name       : {self.name}")
		print(f"Roll No.   : {self.roll_number}")
		print(f"Marks      : {self.marks:.2f}")
		print(f"Grade      : {grade}")
if __name__ == "__main__":
	try:
		name_input = input("Enter student name: ").strip()
		roll_input = int(input("Enter roll number (integer): ").strip())
		marks_input = float(input("Enter marks (0-100): ").strip())
		student = Student(name_input, roll_input, marks_input)
		student.display_details()
	except Exception as exc:
		print(f"Error: {exc}")


