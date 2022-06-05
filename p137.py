import json
n = int(input())

l1 = []
for i in range(n):
    x = input()
    y = json.dumps(x)
    l1.append(y)

print(l1)
y1 = json.dumps(x[0])
y2 = json.dumps(x[1])
y3 = json.dumps(x[2])
y4 = json.dumps(x[3])
print(y3)
print(y4)