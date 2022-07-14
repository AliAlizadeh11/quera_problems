def is_prime(n):
    if n > 1:
        for i in range(2,n):
            if (n % i) == 0:
                return False
                break
        else:
            return True
    else:
        return False

n = int(input())

if is_prime(n) == True and n % 2 != 0:
    print('zoj')
else:
    print('fard')

