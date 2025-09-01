def sum_to_n_for_loop(n):
    # Using for loop with range
    total = 0
    for i in range(1, n + 1):
        total += i
    return total

if __name__ == "__main__":
    n = int(input("Enter a number: "))
    result = sum_to_n_for_loop(n)
    print(f"Sum: {result}")  