def is_prime(n):
    if n == 1:
        return False
    elif n < 4:
        return True
    elif n % 2 == 0:
        return False
    elif n < 9:
        return True
    if n % 3 == 0:
        return False
    else:
        r = int(n ** 0.5)
        f = 5
        while f <= r:
            if n % f == 0:
                return False
            elif n % (f + 2) == 0:
                return False
            f += 6
        return True

def is_circular(n):
    n = list(str(n))
    if len([x for x in "2468" if x in n]) != 0:
        return False
    for i in range(len(n)):
        t = n[0]
        for j in range(len(n) - 1):
            n[j] = n[j + 1]
        n[-1] = t
        if not is_prime(int("".join(n))):
            return False
    return True

count = 1
for x in range(3, 1000000, 2):
    if is_circular(x):
        count += 1
print(count)
