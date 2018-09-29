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

def get_prime_factors(n):
    factors = []
    for x in range(1, int(n ** 0.5)):
        if n % x == 0:
            xc = n // x
            if is_prime(x) and x not in factors:
                factors.append(x)
            if is_prime(xc) and xc not in factors:
                factors.append(xc)
    return factors

number = 4

last_result = False
count = 0

n = 0

while True:
    if len(get_prime_factors(n)) == number:
        last_result = True
        count += 1
        if count == number:
            print(", ".join([str(x) for x in range(n - number + 1, n + 1)]))
            break
    elif last_result:
        last_result = False
        count = 0
        
    n += 1
    
