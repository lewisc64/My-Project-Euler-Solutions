def collatz(n):
    sequence = [n]
    while sequence[-1] != 1:
        if sequence[-1] % 2 == 0:
            sequence.append(sequence[-1] // 2)
        else:
            sequence.append(3 * sequence[-1] + 1)
    return sequence
largest = 0
largest_start = 0
for n in range(1, 1000000):
    l = collatz(n)
    if len(l) > largest:
        largest = len(l)
        largest_start = n
print(largest_start)
