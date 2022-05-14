n = input()
if len(n) <= 100:
    for i in range(len(n)):
        a = n[i]
        b = a * int(n[i])
        print(f"{a}: {b}")