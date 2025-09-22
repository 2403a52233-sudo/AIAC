def area_of_rectangle(length: float, breadth: float) -> float:
    """Calculate the area of a rectangle.

    Args:
        length (float): The length of the rectangle.
        breadth (float): The breadth of the rectangle.

    Returns:
        float: The area of the rectangle.

    Raises:
        ValueError: If length or breadth is not positive.
    """
    if length <= 0 or breadth <= 0:
        raise ValueError("Length and breadth must be positive numbers.")
    return length * breadth

length = 10
breadth = 20
area = area_of_rectangle(length, breadth)
print(f"The area of a rectangle with length {length} and breadth {breadth} is {area}.")

