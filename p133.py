m1, d1 = input().split()
m2, d2 = input().split()
m1 = int(m1)
m2 = int(m2)
d1 = int(d1)
d2 = int(d2)

if m1 >= 1 and m1 <= 6:
    x = (m1 - 1) * 31 + d1
if m2 >= 1 and m2 <= 6:
    y = (m2 - 1) * 31 + d2 
    
if m1 >= 7 and m1 <= 11:
    x = (m1 - 7) * 30 + 186 + d1
if m2 >= 7 and m2 <= 11:
    y = (m2 - 7) * 30 + 186 + d2

if m1 == 12:
    x = 336 + d1
    
if m2 == 12:
    y = 336 + d2

print(y - x)
