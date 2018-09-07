
digits = 3

for x in range(10 ** digits, 10 ** (digits - 1), -1):
    p = int(str(x) + str(x)[::-1])
    print(p)
    for n in range(10 ** (digits - 1), 10 ** digits):
        if p % n == 0 and len(str(p // n)) == digits:
            print("{} = {} * {}".format(p, n, p // n))
            break
    else:
        continue
    break
