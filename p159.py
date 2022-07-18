def digit_root(n):
    if n == 100:
        return 1 
    a = n % 10
    b = (n - a) / 10
    
    return int(a + b)

n = int(input())
print(digit_root(n))