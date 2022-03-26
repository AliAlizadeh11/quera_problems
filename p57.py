n, m = input().split()
n = int(n)
m = int(m)
if n % m == 0:
    print(n // m)
elif n % m != 0:
    if (n % m) < m:
        print((n // m) + 1)
    
    