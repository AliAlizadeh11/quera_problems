n = int(input())
m = input().split()    
m = [int(x) for x in m]

a = int(max(m))
b = int(min(m))

l1 = m[:a+1]
l2 = m[a+1:]

l3 = m[:b+1]
l4 = m[b+1:]

check_max1 = False
check_max1 = False

for i in l1:
    if a >= l1[i]:
        check_max1 = True
for i in l2:
    if a >= l2[i]:
        check_max2 = True
    
check_min3 = False
check_min4 = False

for i in l3:
    if b <= l3[i]:
        check_min3 = True
for i in l4:
    if b <= l4[i]:
        check_min4 = True

result1 = check_max1 and check_max2
result2 = check_min3 and check_min4

if result1 == True or result2 == True:
    print('Yes')
else:
    print('No')