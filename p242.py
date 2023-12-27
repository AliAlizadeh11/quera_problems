t, a, b = list(map(int, input().split()))
def calculate(t, a, b):
    time = 0
    count1 = 0
    count2 = 0
    
    if t == 0:
        return f"{0} {0}"
    
    elif t == 1:
        return f"{1} {0}"
    
    while t != time:
        if time > t:
            return f"{count1} {count2}"
        
        time += 1
        if time <= t:
            count1 += 1
            
        time += a
        time += 1
        
        if time <= t:
            count2 += 1
    
        time += b

    return f"{count1} {count2}"

print(calculate(t, a, b))
