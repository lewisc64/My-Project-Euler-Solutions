def fact(n):
    return (1 if n <= 1 else n * fact(n - 1))

total = 0
for x in range(3, 1000000):
    if sum(map(fact, [int(i) for i in str(x)])) == x:
        print(x)
        total += x
print(total)
