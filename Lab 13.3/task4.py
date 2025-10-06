#List Comprehension Refactoring

# Original approach (verbose)
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
squares_old = []
for i in nums:
    squares_old.append(i * i)

# Refactored with list comprehension (Pythonic)
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
squares = [i * i for i in nums]

# Example usage and comparison
if __name__ == "__main__":
    print("Original approach:")
    print(f"Numbers: {nums}")
    print(f"Squares: {squares_old}")
    
    print("\nList comprehension approach:")
    print(f"Numbers: {nums}")
    print(f"Squares: {squares}")
    
    print("\nAdditional list comprehension examples:")
    # Even squares only
    even_squares = [i * i for i in nums if i % 2 == 0]
    print(f"Even squares: {even_squares}")
    
    # Squares greater than 25
    large_squares = [i * i for i in nums if i * i > 25]
    print(f"Large squares (>25): {large_squares}")
