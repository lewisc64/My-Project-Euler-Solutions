def permutation(n, s1, s2="", j = [0]):
    if j[0] >= n:
        return
    elif len(s1) == 0:
        j[0] += 1
        if j[0] >= n:
            print(s2)
    else:
        for i in range(len(s1)):
            permutation(n, s1[0:i] + s1[i + 1:], s2 + s1[i], j)

permutation(1000000, "0123456789")
