l1 = []
for i in range(4):
    x1 = input().split(" ")
    l1.append(x1[0].upper())
    l1.append(x1[1].upper())
    x1.clear()
    
calculate_R = l1.count('R')
calculate_L = l1.count('L')

if calculate_R == 3:
    z1 = int(l1.index('R')) + 1
    l1[z1:]
    z2 = int(l1.index('R'))
    print(l1[z2])
    
elif calculate_L == 3:
    z1 = int(l1.index('L')) + 1
    l1[z1:]
    z2 = int(l1.index('L'))
    print(l1[z2])

elif calculate_R == 2 and calculate_L == 1:
    a = int(l1.index('R'))
    if a == 1:
        print(l1[0])
    else:
        print(l1[a-1])


        
elif calculate_L == 2 and calculate_R == 1:
    b = int(l1.index('L'))
    if b == 1:
        print(l1[0])
    else:
        print(l1[b-1])
