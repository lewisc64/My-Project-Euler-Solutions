data = open("words.txt", "r")
words = eval("[" + data.read() + "]")
data.close()

def get_score(word):
    return sum([ord(x) - 64 for x in word])

triangle_numbers = [1]
n = 2

while triangle_numbers[-1] < 192:
    triangle_numbers +=[int((1/2) * n * (n + 1))]
    n += 1

triangle_words = []

for word in words:
    if get_score(word) in triangle_numbers:
        triangle_words.append(word)

print(triangle_words)
print(len(triangle_words))
