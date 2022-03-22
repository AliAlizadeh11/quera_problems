n = int(input())
s = ''
for i in range(n):
    l, r = input().split(" ")
    a = range(l, r)
    for j in a:
        if j ** 2 >= l and j ** 2 <= r:
