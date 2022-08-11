a, b, c = list(map(int, input().split()))

def calculate(a : int, b : int, c : int) -> int:
    dish = [a, b, c]
    dish.sort()
    
    condition1 = (dish[2] + dish[0]) / 2 == dish[1]
        
    if a == b == c:
        return 0
    
    elif condition1:
        return 1
    
    else:
        return 2

print(calculate(a, b, c))
