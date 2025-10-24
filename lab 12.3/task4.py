# ...existing code...
def f(x):
    return 2*x**3 + 4*x + 5

def f_prime(x):
    return 6*x**2 + 4

def analyze_minimum():
    # Solve f'(x) = 0 => 6x^2 + 4 = 0
    a, b, c = 6, 0, 4
    disc = b*b - 4*a*c
    if disc < 0:
        print("No real critical points: derivative = 6x^2 + 4 > 0 for all real x.")
        print("f is strictly increasing on R, so there is no finite global minimum.")
        print("Infimum is -infinity as x -> -infinity.")
        # illustrate by evaluating at a large negative x
        for X in (-10, -100, -1000):
            print(f"f({X}) = {f(X)}")
    else:
        # (not expected for this function) compute real roots and evaluate
        import math
        r1 = (-b + math.sqrt(disc)) / (2*a)
        r2 = (-b - math.sqrt(disc)) / (2*a)
        vals = [(r1, f(r1)), (r2, f(r2))]
        best = min(vals, key=lambda t: t[1])
        print(f"Critical points: {vals}")
        print(f"Minimum at x = {best[0]} with f(x) = {best[1]}")

if __name__ == "__main__":
    analyze_minimum()