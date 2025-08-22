def factorial_febo(n):
	"""Return factorial of n and Fibonacci series of n terms.
	Args:
		n (int): Non-negative integer specifying which factorial to compute and how many Fibonacci terms to generate.
	Returns:
		tuple[int, list[int]]: A tuple where the first element is n! and the second is a list of the first n Fibonacci numbers.
	Raises:
		TypeError: If n is not an int.
		ValueError: If n is negative.
	"""
	if not isinstance(n, int):
		raise TypeError("n must be an integer")
	if n < 0:
		raise ValueError("n must be a non-negative integer")
	factorial_result = 1
	for current_value in range(2, n + 1):
		factorial_result *= current_value

	fibonacci_series = []
	if n >= 1:
		fibonacci_series.append(0)
	if n >= 2:
		fibonacci_series.append(1)
	while len(fibonacci_series) < n:
		next_value = fibonacci_series[-1] + fibonacci_series[-2]
		fibonacci_series.append(next_value)
	return factorial_result, fibonacci_series
if __name__ == "__main__":
	try:
		user_input = input("Enter a non-negative integer n: ")
		n_value = int(user_input)
		fact, fibo = factorial_febo(n_value)
		print(f"Factorial of {n_value}: {fact}")
		print(f"Fibonacci series ({n_value} terms): {fibo}")
	except Exception as exc:  # Print friendly error
		print(f"Error: {exc}")


