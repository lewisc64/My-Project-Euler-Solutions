def to_binary(n):
    out = ""
    while n > 0:
        out += str(n % 2)
        n //= 2
    return out

def is_palindrome(s):
    return s == s[::-1]

total = 0
for x in range(1, 1000000, 2):
    if is_palindrome(str(x)) and is_palindrome(to_binary(x)):
        print(x)
        total += x
print(total)
