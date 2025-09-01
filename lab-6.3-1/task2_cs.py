def print_multiples(n):
    for i in range(1, 11):
        print(f"{n} * {i} = {n * i}")

if __name__ == "__main__":
    n = int(input("Enter a number: "))
    print_multiples(n)