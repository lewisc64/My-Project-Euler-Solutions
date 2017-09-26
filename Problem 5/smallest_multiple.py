step = 20
n = step
factors = [x for x in range(1, step) if step % x != 0]
while True:
    valid = True
    for x in factors:
        if n % x != 0:
            n += step
            valid = False
            break
    if valid:
        break
print(n)
