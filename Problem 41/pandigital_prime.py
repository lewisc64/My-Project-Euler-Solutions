def is_pandigital(n):
    return sorted(str(n)) == [str(x) for x in range(1, len(str(n)) + 1)]

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

x = 7654321
while not (is_prime(x) and is_pandigital(x)):
    x -= 1
print(x)
