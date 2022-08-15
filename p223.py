import math

q = int(input())
divisors = list(map(int,input().split()))

def calculate(divisors : list) -> int :
    result = list()
    count_zero = divisors.count(0)
    
    if count_zero != 0:
        new_divisors = [i for i in divisors if i != 0]
        result_mul = math.prod(new_divisors)
    
    result_mul = math.prod(divisors)
    count = 1
    
    while True:
        number = count * result_mul
        if number > 1000:
            break
        
        elif 1 <= number <= 1000:
            result.append(number)
            count += 1
        
    return len(result)

print(calculate(divisors))
        
        
