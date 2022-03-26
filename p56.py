l = input().split()
l = [int(x) for x in l]
result = 0
a = l[0] > 0 and l[1] > 0 and l[2] > 0
b = l[0] < 360 and l[1] < 360 and l[2] < 360
if a and b:
    result += l[0] + l[1] + l[2]
    if result == 180:
        print('Yes')
    elif result != 180:
        print('No')
else:
    print('No')