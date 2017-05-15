s = "".join([str(x) for x in range(1000001)])
out = 1
print(s[12])
for p in range(1,7):
    out *= int(s[10 ** p])
print(out)
