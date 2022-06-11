import re


n = int(input())
l1 = list(map(int,input().split()))
l2 = list(map(int,input().split()))

result = 0
for i in range(n):
    a = l1[i] * l2[i]
    result += a
    
print(result)
