import math
count = 0
def perfect_number(number):
    root = math.sqrt(number)
    if int(root + 0.5) ** 2 == number:
        count += 1
    else:
        pass
    
def seperator(l):
    return ([[l[i],l[i+1]] for i in range(0,len(l),2)])


q = int(input())
l1 = list()

for _ in range(q):
    a = list(map(int, input().split()))
    l1.extend(a)

l2 = seperator(l1)
print(l2)

for i in l2:
    for j in range(len(i)):
        print(i[j])
        perfect_number(i[j])

print(count)