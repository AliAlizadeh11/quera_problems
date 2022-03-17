a, b = input().split()
a = int(a)
b = int(b)
c = a - b
if a == b:
    print('Saal Noo Mobarak!')
if c == -1:
    if a == 0:
        print('R')
    else:
        print('R')
if c == 1:
    if a == 1:
        print('L')
    else:
        print('L')
elif c == -2:
    print('RR')
elif c == 2:
    print('LL')