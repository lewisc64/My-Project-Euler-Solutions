# What I think:
# a and b are prime or 1.
# (-(1)+sqrt((1)^2 - 4*(41)))/(2)
#  = -0.5 + 6.38357267 i
# (-(-79)+sqrt((-79)^2 - 4*(1601)))/(2)
#  = 39.5 + 6.38357267 i
# Hypothysis: When i = 6.38357267, x^2 + ax + b produces some primes.

class ComplexNumber:
    def __init__(self, n, i = 0):
        self.n = n
        self.i = i
    
    def __str__(self):
        return str(self.n) + " + " + str(self.i) + "i"
    
    def __add__(self, c):
        return ComplexNumber(self.n + c.n, self.i + c.i)
    
    def __sub__(self, c):
        return ComplexNumber(self.n - c.n, self.i - c.i)
    
    def __mul__(self, c):
        return ComplexNumber((self.n * c.n) - (self.i * c.i), (self.n * c.i) + (self.i * c.n))
    
    def __truediv__(self, c):
        if type(c) is int:
            return ComplexNumber(self.n / c, self.i / c)

def is_prime(n):
    if n == 1:
        return False
    elif n < 4:
        return True
    elif n % 2 == 0:
        return False
    elif n < 9:
        return True
    elif n % 3 == 0:
        return False
    else:
        r = int(n ** 0.5)
        f = 5
        while f <= r:
            if n % f == 0:
                return False
            elif n % (f + 2) == 0:
                return False
            f += 6
        return True

def sqrt(n):
    if n < 0:
        return ComplexNumber(0, abs(n) ** 0.5)
    else:
        return ComplexNumber(n ** 0.5)

# x^2 + ax + b
def get_root(a, b):
    return ((ComplexNumber(0)-ComplexNumber(a))+sqrt(a * a - 4 * b))/2

def to_string(a, b):
    return "n^2" + (" - " if a < 0 else " + ") + str(abs(a)) + "n"  + (" - " if b < 0 else " + ") + str(abs(b))

def apply_quadratic(a, b, n):
    return n ** 2 + a * n + b

root_i = get_root(1, 41).i

longest_run = 0
longest_a = 0
longest_b = 0

for a in range(1, 1000):
    if a == 1 or is_prime(a):
        for sign_a in range(-1, 2, 2):
            for b in range(1,1001):
                for sign_b in range(-1, 2, 2):
                    ra = a * sign_a
                    rb = b * sign_b
                    root = get_root(ra, rb)
                    if root.i == root_i:
                        print(to_string(ra, rb))
                        n = 0
                        while is_prime(apply_quadratic(ra, rb, n)):
                            n += 1
                        if n > longest_run:
                            longest_run = n
                            longest_a = ra
                            longest_b = rb

print("\nlongest = " + to_string(longest_a, longest_b))
print("Produces " + str(longest_run) + " primes.")
print("a * b = " + str(longest_a * longest_b))
