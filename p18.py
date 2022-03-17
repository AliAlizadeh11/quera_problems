n = int(input())
a = []

for i in range(n):
    s = input()
    t = ''
    for ch in s:
        if ch not in t:
            t += ch
    t += ','
    a.append(t)
    
b = max(a, key = len)
print(len(b) - 1)