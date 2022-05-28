n, t = input().split()
l1 = []
for i in range(int(n)):
    a = input()
    l1.append(a)


b = {}
for j in range(len(l1)):
    z = list(set(t)).difference(set(l1[j]))
    if z == b:
        print("yes")
    else:
        print("no")

print(t)
print(l1)
