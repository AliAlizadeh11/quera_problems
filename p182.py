n = int(input())
l1 = ""
for i in range(n):
    m = input()
    l1+= m
    
l2 = l1.split("CAPS")

def calculate(l1, l2):
    result = ""
    for i, j in enumerate(l2):
        if i%2 == 0:
            result += j.lower()
            
        elif i%2 == 1:
            result += j.upper()
            
    return result

print(calculate(l1, l2))