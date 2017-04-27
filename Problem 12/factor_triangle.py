def get_factors(n):
    factors = []
    for x in range(1, int(n ** 0.5)):
        if n % x == 0:
            factors.append(x)
            factors.append(n / x)
    return factors

amount = 500
n = 1
increment = 2
while True:
    if n % 2 == 0:
        if len(get_factors(n)) >= amount:
            print(n)
            break
    n += increment
    increment += 1
