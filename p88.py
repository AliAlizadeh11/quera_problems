n, x ,y = input().split()
n = int(n)
x = int(x)
y = int(y)

i = 0
while i * x <= n:
    if (n - (i * x)) % y == 0:
        a = i
        b = int((n - (i * x)) / y)
        print(a, b)
    i += 1

print(-1)

