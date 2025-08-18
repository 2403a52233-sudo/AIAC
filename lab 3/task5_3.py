def celsius_to_fahrenheit(c): return c*9/5+32; print(f"Fahrenheit: {celsius_to_fahrenheit(float(input('Enter temperature in Celsius: '))):.2f}")
def celsius_to_fahrenheit(c): return c*9/5+32
print(f"Fahrenheit: {celsius_to_fahrenheit(float(input('Enter temperature in Celsius: '))):.2f}")
import sys

def celsius_to_fahrenheit(celsius: float) -> float:
    """Convert Celsius to Fahrenheit."""
    return celsius * 9 / 5 + 32

if __name__ == "__main__":
    try:
        c = float(input("Enter temperature in Celsius: ").strip())
    except Exception:
        print("Invalid input", file=sys.stderr)
        sys.exit(1)
    print(f"Fahrenheit: {celsius_to_fahrenheit(c):.2f}")


