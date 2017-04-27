import math
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
        r = int(math.sqrt(n))
        f = 5
        while f <= r:
            if n % f == 0:
                return False
            elif n % (f + 2) == 0:
                return False
            f += 6
        return True
  
limit = 2000000
sum = 0
n = 2
while n < limit:
    if is_prime(n):
        sum += n
    n += 1 if n == 2 else 2
print(sum)