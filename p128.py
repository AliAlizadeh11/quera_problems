l = []
for i in range(6):
    a = int(input())
    l.append(a)
r1 = int(min(l[0], l[1]))
r2 = int(min(l[2], l[3]))
r3 = int(min(l[4], l[5]))

print(r1 + r2 + r3)