t, a, b = list(map(int, input().split()))

def calculate(t, a, b):
    result = 0
    count1 = 0
    count2 = 0

    while True:
        if result == t and result != 0:
            break
        
        count1 += 1
        result += (a + 1)
        count2 += 1
        result += (b + 1)
        
    return count1, count2

print(calculate(t, a, b))
