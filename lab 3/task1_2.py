import sys

def compute_factorial(n: int) -> int:
	"""Return n! for a non-negative integer n.

	Raises ValueError for negative inputs.
	"""
	if n < 0:
		raise ValueError("Factorial is not defined for negative integers.")

	result = 1
	for value in range(2, n + 1):
		result *= value
	return result

def main() -> None:
	try:
		text = input("Enter a non-negative integer: ").strip()
		number = int(text)
		print(compute_factorial(number))
	except ValueError as exc:
		print(f"Error: {exc}")
		sys.exit(1)

if __name__ == "__main__":
	main()


