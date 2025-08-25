def factorial(n):
    """
    Calculate the factorial of a given number.
    
    Args:
        n (int): The number to calculate factorial for
        
    Returns:
        int: The factorial of n
        
    Raises:
        ValueError: If n is negative
    """
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    elif n == 0:
        return 1  # 0! = 1 by definition
    else:
        result = 1
        for i in range(1, n + 1):
            result *= i
        return result

def main():
    """Main function to get user input and display factorial result."""
    try:
        
        num = int(input("Enter a number to calculate factorial: "))
        
    
        result = factorial(num)
        
        
        print(f"Factorial of {num} is: {result}")
        
    except ValueError as e:
        if "negative" in str(e):
            print("Error: Factorial is not defined for negative numbers.")
        else:
            print("Error: Please enter a valid integer.")
    except KeyboardInterrupt:
        print("\nProgram interrupted by user.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
