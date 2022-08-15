import math
numbers = list(map(int, input().split()))

def calculate(numbers : list) -> int :
    number = str(math.factorial(numbers[0]))
    result = number.count(str(numbers[1]))
    
    return result

print(calculate(numbers))
