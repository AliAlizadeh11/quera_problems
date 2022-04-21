n = int(input())
k = int(input())
s = input().lower()
s4 = []
i = 0
while i < k:
    s0 = s[-1]
    s1 = s.index(s0)
    s2 = s[:s1]
    s3 = s0 + s2
    for p in range(len(s)):
        s4.extend(s3[p])
    s3.split(" ")
    for j in range(n):
        f = ord(s4[j]) + 1
        if f == 123:
            d = s4.index(chr(f-1))
            s4.pop(d)
            s4.insert(d, 'a')
        elif f != 123:
            s4[j] = chr(f)
    s = "".join(s4).strip()
    i += 1
print(str(s4))