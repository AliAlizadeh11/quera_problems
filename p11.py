t = int(input())
for i in range(t):
    n = int(input())

a = 0
def result(n):
    a = 0
    b = 0
    if n >= 10 and n <= 99:
        a += n % 10
        b += n % 100
    elif n < 10 and n >= 0:
        a += n
    
        
        
    