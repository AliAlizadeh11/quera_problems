n = int(input())
l1 = []
for i in range(n):
    a = input()
    b = a.index(" ")
    c = a[:b]
    c.lower()
    l1.append(c)
l1.sort()
d = {i:l1.count(i) for i in l1}
l2 = []
for j in d.values():
    l2.append(j)
result = max(l2)
if result == 1:
    print(1)
else:
    print(result)