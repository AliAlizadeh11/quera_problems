n = input()
a = 0
b = str(n)
while True:
    for i in range(len(b)):
        a += int(b[i])
    if len(str(a)) == 1:
        print(a)
        break
    else:
        b = str(a)