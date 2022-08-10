import math

q = int(input())
divisors= list(map(int,input().split()))

def calculate(divisors : list) -> int :
    result = list()
    result_mul = math.prod(divisors)
    count = 1
    while True:
        number = count * result_mul
        if number > 1000:
            break
        
        elif number <= 1000:
            result.append(number)
            count += 1
        
    return len(result)

print(calculate(divisors))
        
        
