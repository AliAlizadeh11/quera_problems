p, d = input().split(" ")
d = int(d)
p = int(p)
a = 1
r = d % p
while r > p/2:
    a += 1
    r = (a * d) % p
print(a * d)