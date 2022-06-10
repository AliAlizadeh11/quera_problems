s1 = input()
s2 = list(set(s1))
l1 = list()
l2 = list()
print(s2)
for i in range(len(s2)):
    a = s1.index(s2[i])
    l1.append(a)
    
print(l1)