coins = [200, 100, 50, 20, 10, 5, 2, 1]

def get_total(m):
    return sum(map(int.__mul__, coins, m))

def next_combo(l, target, j = 0):
    if j >= len(l):
        return False
    l[j] += 1
    if get_total(l) > target:
        l[j] = 0
        return next_combo(l, target, j + 1)
    return True

def count_combos(n):
    m = [0, 0, 0, 0, 0, 0, 0, 0]
    total = 0
    while next_combo(m, n):
        if get_total(m) == n:
            #print(" + ".join(list(("£" + str(coins[i] / 100) + " * " + str(m[i])) for i in range(len(m)) if m[i] != 0)))
            total += 1
    return total
print(count_combos(200))
