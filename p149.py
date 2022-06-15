def is_odd(x):
    if x%2 == 0:
        return 0
    else:
        return 1
    
def is_prime_number(y):
    flag = False
    if y > 1:
        for i in range(2, y):
            if (y % i) == 0:
                flag = True
                break
    if flag:
        return 0
    else:
        return 1
    
a = [i for i in range(1000) if is_odd(i) == 1]

for i in range(len(a)):
    if (a[i]**2)%8 ==1:
        print(a[i])