a, b = input().split(" ")
a = int(a)
b = int(b)

h = 12 - a
m = 60 - b
if h == 12 and m == 60:
    print("{:0=2}:{:0=2}".format(a, b))
elif h == 12 and m != 60:
    print("{:0=2}:{:0=2}".format(a, m))
elif h != 12 and m == 60:
    print("{:0=2}:{:0=2}".format(h, b))
else:
    print("{:0=2}:{:0=2}".format(h, m))