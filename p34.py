n = int(input())
m = int(input())

if n in range(100,10000) and m in range(100, 1000):
    n = str(n)
    m = str(m)
    
    if n[::-1] > m[::-1]:
        print(f"{m} < {n}")
    elif n[::-1] < m[::-1]:
        print(f"{n} < {m}")
    else:
        print(f"{m} = {n}")