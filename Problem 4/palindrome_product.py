largest = 0

for a in range(999,100,-1):
    for b in range(999,100,-1):
        n = a * b
        if n > largest and str(n) == str(n)[::-1]:
            largest = n

print(largest)
