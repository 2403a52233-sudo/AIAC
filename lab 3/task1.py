import sys
from typing import List
def compute_factorial(number: int) -> int:
	"""Return factorial of a non-negative integer.

	Raises:
		ValueError: If number is negative.
	"""
	if number < 0:
		raise ValueError("Factorial is not defined for negative numbers")
	result = 1
	for current in range(2, number + 1):
		result *= current
	return result

def parse_number_or_default(argv: List[str], default_value: int) -> int:
	"""Parse integer from argv[1] if present; otherwise return default_value."""
	if len(argv) >= 2 and argv[1].strip() != "":
		try:
			return int(argv[1])
		except ValueError as exc:
			raise ValueError(f"Expected an integer, got: {argv[1]!r}") from exc
	return default_value
    
def main(default_number: int = 5) -> None:
	"""Compute and print factorial for provided number or a default."""
	number = parse_number_or_default(sys.argv, default_number)
	result = compute_factorial(number)
	print(f"Factorial of {number} is {result}")
if __name__ == "__main__":
	main()


