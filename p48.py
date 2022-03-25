l = []
for i in range(3):
    n = int(input())
    l.append(n)
l.sort()
if l[2] ** 2 == l[1] ** 2 + l[0] ** 2:
    print('YES')
else:
    print('NO')
