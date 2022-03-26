l1 = input().split()
l1 = [int(x) for x in l1]

l2 = []
for i in range(l1[0]):
    a = input().split()
    a = [int(x) for x in a]
    start1 = int(a[0])
    end1 = int(a[1])
    l2 = l2 + list(range(start1, end1+1))

l3 = []
for j in range(l1[1]):
    b = input().split()
    b = [int(y) for y in b]
    start2 = int(b[0])
    end2 = int(b[1])
    l3 = l3 + list(range(start2, end2+1))
    
l2 = set(l2)
l3 = set(l3)
result = l2.intersection(l3)
print(len(result))