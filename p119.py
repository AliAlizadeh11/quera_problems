import math
n, k = input().split()
n = int(n)
k = int(k)
i = 0
while i < k:
    a = n / 2
    n = a
    i += 1    
print(math.floor(n))