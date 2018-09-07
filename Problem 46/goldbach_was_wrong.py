def is_prime(n):
    if n == 1:
        return False
    elif n < 4:
        return True
    elif n % 2 == 0:
        return False
    elif n < 9:
        return True
    elif n % 3 == 0:
        return False
    else:
        for f in range(6, int(n ** 0.5) + 2):
            if n % (f - 1) == 0:
                return False
            elif n % (f + 1) == 0:
                return False
        return True

n = 4
while True:
    if not is_prime(n):
        for p in range(2, n):
            if is_prime(p):
                s = ((n - p) / 2) ** 0.5
                if s.is_integer():
                    break
        else:
            if n % 2 == 1:
                print(n)
                break
                
    n += 1
