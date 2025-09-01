def sum_to_n(n):
    total = 0
    i = 1
    while True:
        if i > n:
            break
        total += i
        i += 1
    return total

print(sum_to_n(3))