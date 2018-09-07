# while completely overboard, I like the fact I can use any generators with it.

def triangles():
    n = 0
    while True:
        yield n * (n + 1) // 2
        n += 1

def pentagonals():
    n = 0
    while True:
        yield n * (3 * n - 1) // 2
        n += 1

def hexagonals():
    n = 0
    while True:
        yield n * (2 * n - 1)
        n += 1

start = [285, 165, 143]
generators = [triangles(), pentagonals(), hexagonals()]
values = [next(generators[i]) for i in range(len(generators))]

for i, n in enumerate(start):
    for x in range(n):
        values[i] = next(generators[i])

while True:

    lowest_i = 0
    lowest = max(values)
    for i, value in enumerate(values):
        if value < lowest:
            lowest = value
            lowest_i = i

    values[lowest_i] = next(generators[lowest_i])
    if len([0 for x in values if x == values[0]]) == len(values):
        break

print(values)
