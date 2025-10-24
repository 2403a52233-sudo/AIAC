# ...existing code...
from typing import Tuple, Dict

def solve_chocolate_problem() -> Tuple[float, Dict[str, float]]:
    """Return max profit and production plan (A, B)."""
    # constraints:
    #   A + B <= 5
    #   3A + 2B <= 12
    # corners of feasible region
    corners = [(0.0, 0.0), (4.0, 0.0), (0.0, 5.0), (2.0, 3.0)]

    best_profit = -float("inf")
    best_point = None

    for A, B in corners:
        if A < 0 or B < 0:
            continue
        if A + B <= 5 + 1e-9 and 3*A + 2*B <= 12 + 1e-9:
            profit = 6*A + 5*B
            if profit > best_profit:
                best_profit = profit
                best_point = (A, B)

    if best_point is None:
        raise RuntimeError("No feasible solution found.")

    return best_profit, {"A": best_point[0], "B": best_point[1]}

if __name__ == "__main__":
    profit, vars = solve_chocolate_problem()
    print(f"Maximum profit: ₹{profit}")
    print(f"Produce A = {vars['A']} units, B = {vars['B']} units")
# ...existing code...