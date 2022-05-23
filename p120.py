n = input().split()
n = [int(x) for x in n]
l = [1, 1, 2, 2, 2, 8]
m = []
for i in range(len(n)):
    a = l[i] - n[i]
    m.append(a)
print(*m)
