n = int(input())
power = 0
while n > 2**power:
    if 2 ** power > n:
        break
    power += 1
print(2 ** power)
    