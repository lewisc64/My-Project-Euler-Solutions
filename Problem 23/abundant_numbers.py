import math

def is_abundant(n):
    total = 1
    for f in range(int(math.sqrt(n)), 1, -1):
        if n % f == 0:
            total += f
            d = n // f
            if d != f:
                total += d
            if total > n:
                return True
    return False

def has_sum(n):
    for x in range(1, n // 2 + 1):
        if is_abundant(x):
            y = n - x
            if is_abundant(y):
                return True
    return False

total = 0
for n in range(1, 28123):
    if not has_sum(n):
        total += n
print(total)
