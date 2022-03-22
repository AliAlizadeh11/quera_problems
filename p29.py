import math
def game(number):
    a = number%10
    b = (number - (number % 10)) // 10
    return abs(a - b)

    
    