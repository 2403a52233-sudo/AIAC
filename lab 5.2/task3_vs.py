def fibonacci(n):
    """
    Calculate the nth Fibonacci number using recursion.
    """
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

# Take input from the user
num = int(input("Enter which Fibonacci term to calculate: "))

print(f"Fibonacci({num}) =", fibonacci(num))
