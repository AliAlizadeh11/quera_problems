n = input()
for i in range(len(n)):
    r = (i+1) * n[i] + n[i+1:]
    print(r)