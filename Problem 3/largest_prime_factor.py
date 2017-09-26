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

n = 600851475143
for x in range(int(n ** (1/2)), 0, -1):
    if n % x == 0 and is_prime(x):
        print(x)
        break
