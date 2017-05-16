total = 0
for n in range(2, 1000000):
    s = 0
    for d in str(n):
        s += int(d) ** 5
        if s > n:
            break
    if s == n:
        total += n
print(total)
