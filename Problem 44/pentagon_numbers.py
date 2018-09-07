
def get_pentagon_number(n):
    return n * (3 * n - 1) // 2

def is_pentagonal(x):
    return (((24 * x + 1) ** 0.5 + 1) / 6).is_integer()

j = 0

while True:
    for k in range(j - 1, 0, -1):
        
        pj, pk = get_pentagon_number(j), get_pentagon_number(k)
        
        if is_pentagonal(pj + pk):
            diff = abs(pj - pk)
            if is_pentagonal(diff):
                print("{0} + {1} = {2}, |{0} - {1}| = {3}".format(pj, pk, pj + pk, diff))
                break
    else:
        j += 1
        continue
    break

