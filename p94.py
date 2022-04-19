n = int(input())
l1 = []
for i in range(n):
    m = list(set(input()))
    z = int(len(m))
    l1.append(z)
l1.sort()
print(l1[-1])