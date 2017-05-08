def get_score(name):
    score = 0
    for c in name:
        score += ord(c) - 64
    return score

def merge_sort(a):
    if len(a) <= 1:
        return a
    a1 = merge_sort(a[0:int(len(a) / 2)])
    a2 = merge_sort(a[int(len(a) / 2):])
    return merge(a1, a2)

def merge(a1, a2):
    i = 0
    j = 0
    out = []
    while i < len(a1) or j < len(a2):
        if i != len(a1) and (j == len(a2) or a1[i] < a2[j]):
            out.append(a1[i])
            i += 1
        elif j != len(a2) and (i == len(a1) or a2[j] < a1[i]):
            out.append(a2[j])
            j += 1
        else:
            out.append(a1[i])
            out.append(a2[j])
            i += 1
            j += 1
    return out

file = open("names.txt", "r") # https://projecteuler.net/project/resources/p022_names.txt
names = merge_sort(file.read().replace("\"", "").split(","))
file.close()

total_score = 0
for i in range(0, len(names)):
    total_score += (i + 1) * get_score(names[i])

print(total_score)
