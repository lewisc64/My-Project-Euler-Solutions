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

digits = 4

for x in range(10 ** (digits - 1), 10 ** digits):

    d = 1
    while x + 2 * d < 10 ** digits:
        numbers = [x, x + d, x + d * 2]
        if len(list(filter(is_prime, numbers))) == 3:
            for i in range(1, len(numbers)):
                if sorted(str(numbers[i])) != sorted(str(numbers[i - 1])):
                    break
            else:
                print(numbers)
                print("".join([str(x) for x in numbers]))
        d += 1
