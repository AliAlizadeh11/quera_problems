n = input()

def calculate(n):
    n = str(n)
    
    while len(n) != 1:
        count = 0
        for i in n:
            count += int(i)
        
        n = str(count)
        
    return n

print(calculate(n))