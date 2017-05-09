n1 = 1
n2 = 1
i = 2
while len(str(n2)) < 1000:
    t = n1
    n1 = n2
    n2 = t + n2
    i += 1
print(i)
