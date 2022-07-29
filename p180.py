n = int(input())

for i in range(n):
    l = [i +' ' for i in str(11**i)]
    print(*l)
