def check(first_str, second_str):
    for item in second_str:
        if item in first_str:
            continue
        return 'NO'
    
    count = list()
    for item in second_str:
        count.append(first_str.count(item))
    
    check_item = False
    number = 0
    for item in second_str:
        if first_str.index(item) >= number:
            number += first_str.index(item)
        else:
            check_item = True
    
    for item in second_str[::-1]:
        if first_str.index(item) >= number:
            number += first_str.index(item)
        else:
            check_item = True
            
    if check_item:
        return 'YES'
    else:
        return 'NO'

output = list()
n = int(input())
for i in range(2*n):
    first_str = input()
    second_str = input()
    output.append(check(first_str, second_str))
    
print(output)