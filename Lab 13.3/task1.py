# Refactored version with dictionary-based dispatch
import math
def calculate_rectangle_area(length, width):
    """Calculate the area of a rectangle."""
    return length * width

def calculate_square_area(side):
    """Calculate the area of a square."""
    return side * side
def calculate_circle_area(radius):
    """Calculate the area of a circle."""
    return math.pi * radius * radius
# Dictionary-based dispatch for cleaner code
SHAPE_CALCULATORS = {
    "rectangle": calculate_rectangle_area,
    "square": calculate_square_area,
    "circle": calculate_circle_area
}
def calculate_area_dict_dispatch(shape, x, y=0):
    """
    Calculate area using dictionary-based dispatch.
    
    Args:
        shape (str): Type of shape ("rectangle", "square", "circle")
        x (float): Primary dimension (length/side/radius)
        y (float): Secondary dimension for rectangle (width) 
    Returns:
        float: Area of the shape
      
    Raises:
        ValueError: If shape is not supported
    """
    if shape not in SHAPE_CALCULATORS:
        raise ValueError(f"Unsupported shape: {shape}. Supported shapes: {list(SHAPE_CALCULATORS.keys())}")
    calculator = SHAPE_CALCULATORS[shape]
    if shape == "rectangle":
        return calculator(x, y)
    else:
        return calculator(x)
# Example usage
if __name__ == "__main__":
    print(f"Rectangle area: {calculate_area_dict_dispatch('rectangle', 5, 3)}")
    print(f"Circle area: {calculate_area_dict_dispatch('circle', 2)}")
    print(f"Square area: {calculate_area_dict_dispatch('square', 4)}")

