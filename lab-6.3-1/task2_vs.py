def print_multiples(num):
    for i in range(1, 11):
        print(num * i)

if __name__ == "__main__":
    num = int(input("Enter a number: "))
    print_multiples(num)