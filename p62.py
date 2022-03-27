import math
n = int(input())

def isPerfectSquare(x):
    s = int(math.sqrt(x))
    return s*s == x

def isFibonacci(n):
    return isPerfectSquare(5*n*n + 4) or isPerfectSquare(5*n*n - 4)
for i in range(n):
    if (isFibonacci(i+1) == True):
        print('+', end='')
    else:
        print ('-', end='')