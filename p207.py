t = int(input())

numbers = list()
for _ in range(t):
    number = input()
    numbers.append(number)


def condition1(number : str) -> bool:
    unique_number = list(set(number))
    for item in unique_number:
        if number.count(item) >= 4:
            return True
        
    return False

def condition2(number : str) -> bool:
    if len(list(set(list(number[0:3])))) == 1:
        return True
    
    elif len(list(set(list(number[1:4])))) == 1:
        return True

    elif len(list(set(list(number[2:5])))) == 1:
        return True

    elif len(list(set(list(number[3:6])))) == 1:
        return True
    
    elif len(list(set(list(number[4:7])))) == 1:
        return True
    
    elif len(list(set(list(number[5:8])))) == 1:
        return True
    
    else:
        return False
    
def condition3(number : str) -> bool:
    if number == number[::-1]:
        return True
    
    else:
        return False

def check(numbers : list) -> str:
    result = list()
    for item in numbers:
        condition_list = [condition1(item), condition2(item), condition3(item)]
        if any(condition_list):
            result.append('Ronde!')
        
        else:
            result.append('Rond Nist')
            
    return result


for i in check(numbers):
    print(i)