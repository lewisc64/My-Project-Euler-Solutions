def fact(n):
    out = 1
    for n in range(2,n + 1):
        out *= n
    return out

def choose(n, k):
    return fact(n)/(fact(k) * fact(n - k))

size = 20
print(choose(size * 2, size))
