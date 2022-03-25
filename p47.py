n = int(input())
l = []
for i in range(n):
    m = input()
    l.append(m)
l.sort()
print("".join(l[-1]))