n = int(input())
numbers = list(map(int, input().split()))

count = 0
for item in numbers:
    if item >= 0:
        calculate = item
    else:
        calculate = -1 * item
        
    count += calculate
    
print(count)

