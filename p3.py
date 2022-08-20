import math
n = int(input())
x = list()
y = list()

for i in range(n):
    a, b = list(map(float, input().split()))
    x.append(max(a))
    y.append(max(b))

c = int(max(max(x), max(y))) + 1
result = c * (2**(1/2))

if result >= int(result) + 0.5:
    print(math.ceil(result))
else:
    print(math.floor(result))   