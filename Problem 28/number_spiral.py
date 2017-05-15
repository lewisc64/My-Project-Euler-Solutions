n = 1
increment = 2
total = 1
max_side = 1001
for side in range(3, max_side + 1, 2):
    for x in range(1, 5):
        n += increment
        total += n
    increment += 2
print(total)
