import math
n = int(input())
l = list(map(int, input().split()))  
a = math.gcd(*l)
result2 = 0
for item in range(len(l)):
    result1 = int(l[item]) / int(a)
    result2 +=  result1
print(int(result2))
