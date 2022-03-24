n = int(input())
power = 1
number = 2
result = number ** power
while n > result:
    result = number ** power
    if result > n:
        break
    power += 1
    
print(result)