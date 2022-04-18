n = int(input())
m1 = input().split()
m1 = [int(x) for x in m1]

m2 = set(m1)
for i in range(len(m2)):
    m1.count(m2[i])
    