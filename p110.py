x1 = input().split()
x2 = input().split()
x3 = input().split()
x4 = input().split()

x = x1 + x2 + x3 + x4
y = {x[i]:x[i+1] for i in range(0, len(x), 2) if x[i+1] != 'U'}

l = list(y.values())
l1 = ['R', 'L', 'R']
l2 = ['L', 'R', 'L']
l3 = ['R', 'R', 'L']
l4 = ['L', 'L', 'R']

r1 = list(y.keys())[0]
r2 = list(y.keys())[1]

if l == l1:
    print("".join(r1))

elif l == l2:
    print("".join(r1))
    
elif l == l3:
    print("".join(r1))

elif l == l4:
    print("".join(r1))

else:
    print("".join(r2))