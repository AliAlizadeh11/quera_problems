n = int(input())
numbers = list()
for _ in range(n):
    number = int(input())
    numbers.append(number)

def lcm(lst : list) -> int :
    lcm_temp = max(lst)
    
    while(True):
        if all(lcm_temp % x == 0 for x in lst):
            break
        
        lcm_temp = lcm_temp + 1
        
    return lcm_temp


def calculate_answer(num : int) -> int :
    result = num % 30
    
    return result + 1

print(calculate_answer(lcm(numbers)))
