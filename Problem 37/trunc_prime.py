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

def is_trunc_prime(s, m = 0):
    if s == "":
        return True
    elif m == 0:
        return len(s) != 1 and is_trunc_prime(s, -1) and is_trunc_prime(s, 1)
    elif is_prime(int(s)):
        if m == 1:
            return is_trunc_prime(s[1:], 1)
        else:
            return is_trunc_prime(s[:len(s) - 1], -1)
    else:
        return False

total = 0
count = 0
x = 11
while count < 11:
    if is_trunc_prime(str(x)):
        print(x)
        count += 1
        total += x
    x += 2
print(total)
