n = int(input())
l = []
l.append("*")
for i in range(n):
    # for j in range(n - i):
    #     print(" ", end = '')
    for j in range(i):
        print(" ", end = '')
        print("*", end = '')
    for j in range(i):
        print("*", end = '')
    print("*")