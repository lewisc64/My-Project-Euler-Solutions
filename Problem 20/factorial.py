def factorial(n):
    out = 1
    for x in range(2, n + 1):
        out *= x
    return out

def sum_digits(n):
    sum = 0
    for d in str(n):
        sum += int(d)
    return sum

print(sum_digits(factorial(100)))
