l1 = []
for i in range(5):
    a = input()
    l1.append(a)
l2 = []
for i in range(len(l1)):
    if 'MOLANA' in str(l1):
        l2.append(i+1)
    if 'HAFEZ' in str(l1):
        l2.append(i+1)
        
l2.sort()
l2 = set(l2)
print(*l2)