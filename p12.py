import math
l = []
k = []
n = int(input())
for i in range(n):
    m = int(input())
    l.append(m)
while len(k) != 1:   
    for j in l:
        h = l[j+1] - l[j]
        k.append(h)
    if len(k) == 1:
        break

output = math.abs(k[0])
print(output%(10 ** 9 + 7))