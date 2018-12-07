
divisors = [2, 3, 5, 7, 11, 13, 17]

total = 0

for n in range(1000000000, 10000000000):
    s = str(n)
    if sorted(s) == list("0123456789"):
        for i, div in zip(range(1, len(s) - 2), divisors):
            sub = s[i:i+3]
            if int(sub) % div != 0:
                break
        else:
            total += n

print(total)