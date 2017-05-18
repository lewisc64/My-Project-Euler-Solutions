def get_factor_pairs(n):
    pairs = []
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            pairs.append((i, n // i))
    return pairs

products = []
for x in range(1000, 10000):
    for pair in get_factor_pairs(x):
        s = str(pair[0]) + str(pair[1]) + str(x)
        if len(s) == 9 and sorted(s) == list("123456789"):
            print(str(pair[0]) + " * " + str(pair[1]) + " = " + str(x))
            if x not in products:
                products.append(x)
print(sum(products))
