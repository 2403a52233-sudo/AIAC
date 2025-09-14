def add(a, b):
    # Returns the sum of a and b
    return a + b

def subtract(a, b):
    # Returns the difference of a and b
    return a - b

def multiply(a, b):
    # Returns the product of a and b
    return a * b

def divide(a, b):
    """
    Divides two numbers and returns the result.
    Parameters:
        a (float or int): The numerator.
        b (float or int): The denominator.
    Returns:
        float: The result of dividing a by b.
    Raises:
        ValueError: If b is zero.
    """
    if b == 0:
        # Raise an error if denominator is zero
        raise ValueError("Cannot divide by zero.")
    return a / b

if __name__ == "__main__":
    # Prompt user to enter two numbers
    x = float(input("Enter first number: "))
    y = float(input("Enter second number: "))
    # Display results of all operations
    print("Add:", add(x, y))
    print("Subtract:", subtract(x, y))
    print("Multiply:", multiply(x, y))
    print("Divide:", divide(x, y))