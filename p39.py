x1, y1 = input().split(" ")
x2, y2 = input().split(" ")
x3, y3 = input().split(" ")
x1 = int(x1)
x2 = int(x2)
x3 = int(x3)
y1 = int(y1)
y2 = int(y2)
y3 = int(y3)

x4 = 0
y4 = 0
if x1 == x2 or x1 == x3:
    if x1 == x2:
        x4 = x3
    else:
        x4 = x2
else:
    x4 = x1

if y1 == y2 or y1 == y3:
    if y1 == y2:
        y4 = y3
    else:
        y4 = y2
else:
    y4 = y1

print(f"{x4} {y4}")