try:
    squares = []
    with open("numbers.txt", "r") as f:
        for line in f:
            token = line.strip()
            if not token:
                continue
            try:
                num = int(token)
            except ValueError:
                continue
            squares.append(num * num)

    with open("squares.txt", "w") as f2:
        for sq in squares:
            f2.write(str(sq) + "\n")

    print("Squares written")
except FileNotFoundError:
    print("Error: numbers.txt not found")
except Exception as e:
    print(f"An error occurred: {e}")
