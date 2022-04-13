n, m = input().split()
k = input().split()
k = int(k[0])

l = []
for x in range(int(k)):
    a = input().split()
    a = [int(b) for b in a]
    l.append(a)

map = []
for x in range(int(n)):
    map.append([])
    for y in range(int(m)):
        map[x].append(0)