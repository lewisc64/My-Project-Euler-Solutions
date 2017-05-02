import re

numbers = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
powers = {0:"", 1:"ten", 2:"hundred", 3:"thousand", 6:"million"}
replacements = [["zero( [a-z]+)?", ""],
                ["one ten", "ten"],
                ["two ten", "twenty"],
                ["three ten", "thirty"],
                ["four ten", "forty"],
                ["five ten", "fifty"],
                ["six ten", "sixty"],
                ["seven ten", "seventy"],
                ["eight ten", "eighty"],
                ["nine ten", "ninety"],
                ["ten one", "eleven"],
                ["ten two", "twelve"],
                ["ten three", "thirteen"],
                ["ten four", "fourteen"],
                ["ten five", "fifteen"],
                ["ten six", "sixteen"],
                ["ten seven", "seventeen"],
                ["ten eight", "eighteen"],
                ["ten nine", "nineteen"],
                ["  ", " "],
                [" +$", ""],
                [" +and$", ""]]

def get_power(n):
    actual = len(str(n)) - 1
    power = 0
    left = 0
    for key in powers:
        if key <= actual:
            power = key
            left = actual - key
    return power, left

def to_string(n):
    n = str(n)
    slicer = 0
    out = ""
    while slicer < len(n):
        power, left = get_power(n[slicer:])
        out += numbers[int(n[slicer])] + " "
        if left == 0:
            out += powers[power] + (" and " if power == 2 else " ")
        else:
            out += powers[left] + " "
        slicer += 1
    for replacement in replacements:
        out = re.sub(replacement[0], replacement[1], out)
    return out

def count(s):
  count = 0
  for c in s:
    if c != " " and c != "-":
      count += 1
  return count

total = 0
for n in range(1,1001):
  print("'" + to_string(n) + "'")
  total += count(to_string(n))

print(total)
