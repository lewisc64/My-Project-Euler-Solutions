def sum_digits(n):
    return sum([int(x) for x in str(n)])

biggest = 0

for a in range(100):
    for b in range(100):
        v = sum_digits(a**b)
        if v > biggest:
            biggest = v

print(biggest)