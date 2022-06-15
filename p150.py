n = int(input())
l1 = list(map(int, input().split()))
l2 = list(map(int, input().split()))

l3 = list()
for i in zip(l1, l2):
    if i[1] == 1:
        l3.append(i[0])

l3.sort()
print(*l3)