def calc_average(marks):
	"""Return the average of a list of numeric marks.

	Raises ValueError if marks is empty.
	"""
	if not marks:
		raise ValueError("marks list is empty")
	total = 0
	for m in marks:
		total += m
	average = total / len(marks)
	return average


marks = [85, 90, 78, 92]
print("Average Score is", calc_average(marks))