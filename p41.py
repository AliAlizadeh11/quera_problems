l1, r1 = input().upper().split()
l2, r2 = input().upper().split()
if l1 == r1 or l2 == r2:
    print('YES')
elif l1 == r2 or l2 == r1:
    print('YES')
else:
    print('NO')

    

