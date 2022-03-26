n = int(input())
l = []
for i in range(n):
    a = int(input())
    l.append(a)
average = int(sum(l) / len(l))
result = 0
for i in range(len(l)):
    if int(l[i]) < average:
        b = average - int(l[i])
        result += b
print(int(result))
        