def bubble_sort(arr):
    """
    Implements bubble sort algorithm to sort an array in ascending order
    Args:
        arr: List of elements to be sorted
    Returns:
        Sorted list
    """
    n = len(arr)
    for i in range(n):
        # Flag to optimize if array is already sorted
        swapped = False
        
        # Last i elements are already in place
        for j in range(0, n-i-1):
            # Compare adjacent elements
            if arr[j] > arr[j+1]:
                # Swap if elements are in wrong order
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        
        # If no swapping occurred, array is already sorted
        if not swapped:
            break
    
    return arr

# Test the function
if __name__ == "__main__":
    # Example usage
    numbers = [64, 34, 25, 12, 22, 11, 90]
    print("Original array:", numbers)
    
    sorted_numbers = bubble_sort(numbers)
    print("Sorted array:", sorted_numbers)