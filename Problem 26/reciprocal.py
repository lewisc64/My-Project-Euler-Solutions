def reciprocal(div):
    if div == 1:
        return "1.0r0r"
    result = "0." + "0" * (len(str(div)) - 1)
    n = int(str(10) + "0" * len(str(div)))
    processed = []
    while True:
        r = n % div
        if r == n:
            n *= 10
            add = "0"
        else:
            add = str(n // div)
            n = r * (1 if r == 0 else 10)
        if (add, n) in processed:
            result += "r"
            for j in range(len(processed)):
                if processed[j] == (add, n):
                    i = j + len(str(div)) + 2
            result = result[:i] + "r" + result[i:]
            return result
        else:
            processed.append((add, n))
        result += add
        
    return result

def get_repeating(s):
    out = ""
    rec = False
    for c in s:
        if rec:
            out += c
        if c == "r":
            rec = not rec
            if not rec:
                return out[:len(out) - 1]

longest = 0
longest_d = 0
for d in range(1,1000):
    repeat = len(get_repeating(reciprocal(d)))
    if repeat > longest:
        longest = repeat
        longest_d = d
print(longest_d)
