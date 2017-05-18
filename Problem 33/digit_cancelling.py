n = 1
d = 1
for i in range(10,100):
    for j in range(10, 100):
        if j > i:
            for x in range(1, 10):
                if str(x) in str(i) and str(x) in str(j):
                    n1 = int(str(i).replace(str(x), "", 1))
                    n2 = int(str(j).replace(str(x), "" , 1))
                    if n2 != 0 and n1 / n2 == i / j:
                        n *= n1
                        d *= n2
                        print(str(i) + "/" + str(j) + " = " + str(n1) + "/" + str(n2))
print(str(n) + "/" + str(d))
