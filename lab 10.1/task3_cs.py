def calculate_percentage_value(base_amount: float, percentage: float) -> float:
    """
    Calculate the percentage value of a given amount.
    
    Args:
        base_amount: The original amount
        percentage: The percentage to calculate (e.g., 15 for 15%)
    
    Returns:
        The calculated percentage value
        
    Raises:
        ValueError: If inputs are negative
    """
    # Check for negative values only
    if base_amount < 0 or percentage < 0:
        raise ValueError("Values cannot be negative")
    
    return base_amount * percentage / 100
# Define the base amount and percentage
base_amount: float = 200
percentage_rate: float = 15

try:
    # Calculate and display the percentage value
    percentage_value: float = calculate_percentage_value(base_amount, percentage_rate)
    print(f"The {percentage_rate}% of {base_amount} is: {percentage_value}")
    
except ValueError as e:
    print(f"Error: {e}")
