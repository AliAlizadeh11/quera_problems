a, b, l = input().split()
a = int(a)
b = int(b)
l = int(l)
result = 0
count = 0
for i in range(l):
    result += a
    count += 1
    if count == l:
        print(result)
        break
    result += b
    count += 1
    if count == l:
        print(result)
        break

