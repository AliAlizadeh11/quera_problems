import math
x = 7
a = math.ceil(math.pow(x, 5/3) + math.tan(math.radians(x)))
b = math.floor(math.pow(math.pi, 2 + math.atan(math.pow(math.sin(math.radians(x)), 2))))
print(math.gcd(a, b))
