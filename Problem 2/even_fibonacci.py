a, b = 1, 2
sum_evens = 2
while b < 4000000:
    n = a + b
    if n % 2 == 0:
        sum_evens += n
    a, b = b, n
print(sum_evens)
