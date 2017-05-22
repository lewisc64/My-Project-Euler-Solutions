l = 0
l_p = 0
for p in range(1, 1000):
    s = 0
    for a in range(1, p):
        for b in range(1, a):
            c = (a ** 2 - b ** 2) ** 0.5
            if a + b + c == p:
                s += 1
    if s > l:
        l = s
        l_p = p
print(l_p)
