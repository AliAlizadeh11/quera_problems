x1, y1, x2, y2 = input().split()
if int(y1) == int(y2):
    print('Horizontal')
elif int(x1) == int(x2):
    print('Vertical')
else:
    print('Try again')
    