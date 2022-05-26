n, m = input().split()
n = int(n)
m = int(m)

l1 = []
for i in range(n):
    a = input().split()
    l1.append(a[0])
    l1.append(a[1])
    a.clear()

b = {l1[i]:l1[i+1] for i in range(0, int(len(l1)) - 1, 2)}

c = input().split()

d = []
for k in range(len(c)):
    if c[k] in b.keys():
        d.append(b.get(c[k]))
        d.append('kachal!')
    else:
        d.append('kachal!')

print(*d)
