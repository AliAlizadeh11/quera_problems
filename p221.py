n = int(input())
numbers = list(map(int, input().split()))

def calculate(numbers : list) -> int :
    min_number = min(numbers)
    result = 0
    
    for item in numbers:
        if item%min_number == 0:
            result += (item/min_number)
        else:
            result += (item)
    
    return int(result)

print(calculate(numbers))
