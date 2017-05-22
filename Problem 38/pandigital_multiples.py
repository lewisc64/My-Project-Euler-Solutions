digits = [str(x) for x in range(1, 10)]
largest = 0
m = [1]
for i in range(2,10):
    m.append(i)
    s = ""
    n = 0
    while len(s) <= 9:
        s = "".join([str(m[x] * n) for x in range(len(m))])
        if len(s) == 9:
            if int(s) > largest and sorted(s) == digits:
                largest = int(s)
        n += 1
print(largest)
