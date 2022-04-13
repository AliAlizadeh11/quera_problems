r, c = input().split()
r = int(r)
c = int(c)

if c <= 10:
    result1 = 'Right'
else:
    result1 = 'Left'

result2 = 11 - r

if result1 == 'Right':
    result3 = c
else:
    result3 = 21 - c
print(result1, result2, result3)