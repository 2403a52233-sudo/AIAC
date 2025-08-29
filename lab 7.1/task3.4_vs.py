try:
    with open("numbers.txt", "r") as f:
        nums = f.readlines()

    squares = []
    for n in nums:
        n = n.strip()
        try:
            number = int(n)
            squares.append(number ** 2)
        except ValueError:
            continue  # Skip lines that are not valid integers

    with open("squares.txt", "w") as f2:
        for sq in squares:
            f2.write(str(sq) + "\n")

    print("Squares written")
except FileNotFoundError:
    print("Error: 'numbers.txt' not found.")