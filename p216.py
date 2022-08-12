from msilib.schema import Condition


a, b, c, d, e, f = list(map(int, input().split()))

def check(a, b, c, d, e, f):
    first_condition = b >= e and a >= d
    second_condition = b >= e and a >= f
    third_condition = b >= d and a >= e
    fourth_condition = b >= e and a >= f
    
    
    if first_condition or second_condition or third_condition or fourth_condition:
        return 'zende mimuni'
    
    elif first_condition == False and second_condition == False or third_condition == False and fourth_condition == False:
        return 'dari mimiri'

print(check(a, b, c, d, e, f))
