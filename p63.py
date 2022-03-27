n = int(input())
l1 = []
for i in range(n):
    m = int(input())
    l1.append(m)
l2 = []
count = 0
for i in range(len(l1) - 1):
    if int(l1[i]) == int(l1[i+1]):
        continue
    elif int(l1[i]) != int(l1[i+1]):
        count += 1
        
print(count)
