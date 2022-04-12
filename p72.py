n = input().split()
n = [int(x) for x in n]

l1 = input().split()
l1 = [int(x) for x in l1]
r1 = list(range(l1[0],l1[-1]))

l2 = input().split()
l2 = [int(x) for x in l2]
r2 = list(range(l2[0],l2[-1]))

l3 = input().split()
l3 = [int(x) for x in l3]
r3 = list(range(l3[0],l3[-1]))

r1 = set(r1)
r2 = set(r2)
r3 = set(r3)

total1 = r1.difference(r2).difference(r3)
total3 = r1.intersection(r2).intersection(r3)