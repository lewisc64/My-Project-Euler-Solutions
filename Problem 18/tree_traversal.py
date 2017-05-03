text = """75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23"""

def get_tree(lines, i = 0, j = 0):
    line = lines[i].split(" ")
    if i + 1 >= len(lines):
        return [-1, int(line[j]), -1]
    tree = [get_tree(lines, i + 1, j), int(line[j]), get_tree(lines, i + 1, j + 1)]
    return tree

tree = get_tree(text.splitlines())

def get_node(path):
    if path == []:
        return tree[1]
    route = tree[path[0]]
    for i in range(1, len(path)):
        route = route[path[i]]
    try:
        return int(route)
    except:
        return route[1]

def path_lengths(tree, path = [], length = 0, lengths = []):
    node = get_node(path)
    if node == -1:
        lengths.append(length)
        return lengths
    length += get_node(path)
    lengths = path_lengths(tree, path + [0], length, lengths)
    lengths = path_lengths(tree, path + [2], length, lengths)
    return lengths

print(max(path_lengths(tree)))
