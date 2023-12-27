n = int(input())
p = list(map(int, input().split()))

def calculate(n, p):
    min_num = min(p)
    output = sum(p) - ((n-1) * 100)
    
    if output < 0:
        return f"0 {min_num}"
    
    return f"{output} {min_num}"
        

print(calculate(n, p))
