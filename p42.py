T = int(input())
if T in range(-273,6000):
    if T > 100:
        print('Steam')
    elif T < 0:
        print('Ice')
    else:
        print('Water')