import sys


def celsius_to_fahrenheit(celsius: float) -> float:
    return celsius * 9 / 5 + 32


if __name__ == "__main__":
    try:
        temp_c = float(input("Enter temperature in Celsius: ").strip())
    except Exception:
        print("Invalid input. Please enter a number.", file=sys.stderr)
        sys.exit(1)
    print(f"Fahrenheit: {celsius_to_fahrenheit(temp_c):.2f}")


