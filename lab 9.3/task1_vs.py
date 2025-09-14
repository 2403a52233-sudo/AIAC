def sum(n):
    """
    Calculates the sum of even and odd numbers in a given list.
    Args:
        n (list of int): A list of integers to be processed.
    Returns:
        tuple: A tuple containing two integers:
            - The sum of even numbers in the list.
            - The sum of odd numbers in the list.
    Example:
        >>> sum([1, 2, 3, 4])
        (6, 4)
    """
    even = 0  # Initialize sum for even numbers
    odd = 0   # Initialize sum for odd numbers
    for num in n:
        if num % 2 == 0:
            even = even + num  # Add to even sum if number is even
        else:
            odd = odd + num    # Add to odd sum if number is odd
    return even, odd  # Return both sums as a tuple

# Read a line of input, split by spaces, and convert to integers
n = list(map(int, input().split()))
even, odd = sum(n)  # Call the function and unpack the result
print("Even sum:", even)  # Print sum of even numbers
print("Odd sum:", odd)    # Print sum of odd numbers