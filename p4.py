import math
n = int(input())
m = list(map(int, input().split()))

r1 = math.gcd(*m)
r2 = 1
r3 = [r2 *= i for i in m]
    
    
print((r2**r1)%(1000000007))