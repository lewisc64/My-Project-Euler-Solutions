for a in range(1,500):
  for b in range(a + 1,500):
    c = 1000 - a - b
    if c > max(a, b):
      if a ** 2 + b ** 2 == c ** 2:
        print("a = " + str(a))
        print("b = " + str(b))
        print("c = " + str(c))
        print("a + b + c = " + str(a + b + c))
        print("a * b * c = " + str(a * b * c))