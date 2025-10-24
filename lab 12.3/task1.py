def linear_search(arr, target):
    """
    Performs linear search to find target value in array
    Args:
        arr: List of elements to search through
        target: Value to find
    Returns:
        Index of target if found, -1 if not found
    """
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

# Test the function
if __name__ == "__main__":
    # Example usage
    numbers = [5, 2, 9, 1, 7, 6, 3]
    target = 7
    
    result = linear_search(numbers, target)
    if result != -1:
        print(f"Element {target} found at index {result}")
    else:
        print(f"Element {target} not found in the list")