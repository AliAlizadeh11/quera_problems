n = int(input())
l1 = []
l2 = []
l3 = []
for item in range(n):
    a = int(input())
    l1.append(a)
    
for i in range(len(l1)):
    len_number = len(str(l1[i]))
    decrease_number = int(len_number) * 9
    result1 = int(l1[i]) - int(decrease_number)
    
    for j in range(int(result1), int(l1[i]) + 1):
        sum_of_digits = sum(int(digit) for digit in str(j))
        if int(j) + int(sum_of_digits) == int(l1[i]):
            l2.append(0)
        else:
            continue
        
    if len(l2) != 0:
        l3.append('Yes')
    elif len(l2) == 0:
        l3.append('No')
    l2.clear()
for z in range(len(l3)):
    print(l3[z])