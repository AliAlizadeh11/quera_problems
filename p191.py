n = int(input())

def count_divisor(n):
    x = len([i for i in range(1,n+1) if n % i == 0])
    return x

def sum_divisor(n):
    x = sum([i for i in range(1,n+1) if n % i == 0])
    return x

def result(n):
    count = 0
    sum_ = 0
    for item in range(1, n+1):
        count += count_divisor(item)
        sum_ += sum_divisor(item)
        
    return f"{count} {sum_}"

print(result(n))
