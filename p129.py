a, b, c = input().split()
t1 = input().split()
t2 = input().split()
t3 = input().split()

l1 = [int(x) for x in range(int(t1[0]), int(t1[1]))]
l2 = [int(x) for x in range(int(t2[0]), int(t2[1]))]
l3 = [int(x) for x in range(int(t3[0]), int(t3[1]))]

l4 = l1 + l2 + l3
l4.sort()

r1 = {i:l4.count(i) for i in l4}
r2 = list(r1.values())

z1 = r2.count(1)
z2 = r2.count(2)
z3 = r2.count(3)

print((int(a) * z1) + (int(b) * z2 * 2) + (int(c) * z3 * 3))