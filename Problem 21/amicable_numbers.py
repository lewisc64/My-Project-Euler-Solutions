import math

def d(n):
    total = 1
    for f in range(2, int(math.sqrt(n)) + 1):
        if n % f == 0:
            total += f
            total += n / f
    return total

sum_amicable = 0
for n in range(1,10000):
    s = d(n)
    if s != n and d(s) == n:
        sum_amicable += n

print(sum_amicable)
