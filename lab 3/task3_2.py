from typing import List, Optional, Tuple

DEFAULT_SLABS: List[Tuple[Optional[int], float]] = [
    (100, 1.5),   # first 100 units @ 1.5
    (100, 2.5),   # next 100 units @ 2.5 (101-200)
    (300, 4.0),   # next 300 units @ 4.0 (201-500)
    (None, 6.0),  # remaining units @ 6.0 (>500)
]

def calculate_bill(units: int, slabs: List[Tuple[Optional[int], float]] = DEFAULT_SLABS) -> float:
    remaining = max(0, int(units))
    total = 0.0
    for cap, rate in slabs:
        if remaining <= 0:
            break
        take = remaining if cap is None else min(remaining, cap)
        total += take * rate
        remaining -= take
    return round(total, 2)
if __name__ == "__main__":
    raw = input("Enter units consumed: ").strip()
    try:
        units_val = int(float(raw))
    except Exception:
        print("Invalid input. Please enter a numeric value.")
    else:
        total_amount = calculate_bill(units_val)
        print(f"Units consumed: {units_val}, Total current bill: {total_amount}")


