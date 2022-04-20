p, d = input().split()
p = int(p)
d = int(d)
t = 1
r = d % p

while r > (p/2):
	t = t+1
	r = (t*d)%p

print(d*t)