n = int(input())
m = input().split()

for i in range(1, n+1):
    if int(m[i-1]) <= 3:
        print("*" * int(m[i-1]))
    else:
        print("*")