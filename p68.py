l = []
while True:
    n = int(input())
    if n == 0:
        break
    l.append(n)
l.reverse()
for i in range(len(l)):
    print(l[i])