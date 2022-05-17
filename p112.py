import math
n = int(input())
l = []
count = 0
for i in range(n):
    q = input().split()
    for j in range(int(q[0]), int(q[1]) + 1):
        a = math.sqrt(j)
        if int(a + 0.5) ** 2 == j:
            count += 1
    l.append(count)


for j in range(len(l)):
    if l.index(l[j]) == 0:
        print(l[j])
    else:
        o = l[j]
        print(l[j] - sum(l[:o]))