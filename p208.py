x1 = int(input())
v1 = int(input())
x2 = int(input())
v2 = int(input())

def check(x1, x2, v1, v2):
    condition_positions1 = x1 >= x2
    condition_positions2 = x1 <= x2
    condition_velocity1 = v1 > v2 >= 0
    condition_velocity2 = v2 > v1 >= 0
    condition_velocity3 = v1 < v2 <= 0
    condition_velocity4 = v2 < v1 <= 0
    condition_velocity5 = v1 == v2
    condition_velocity6 = v1 < 0 and v2 > 0
    condition_velocity7 = v1 > 0 and v2 < 0
    
    if condition_positions1:
        if condition_velocity1:
            return 'BORO BORO'
    
        elif condition_velocity2:
            return 'SEE YOU'
        
        elif condition_velocity3:
            return 'SEE YOU'
        
        elif condition_velocity4:
            return 'BORO BORO'
        
        elif condition_velocity6:
            return 'SEE YOU'

        elif condition_velocity7:
            return 'BORO BORO'
        
        
    
    if condition_positions2:
        if condition_velocity1:
            return 'SEE YOU'
        
        elif condition_velocity2:
            return 'BORO BORO'
        
        elif condition_velocity3:
            return 'BORO BORO'
        
        elif condition_velocity4:
            return 'SEE YOU'

        elif condition_velocity6:
            return 'BORO BORO'

        elif condition_velocity7:
            return 'SEE YOU'
        
    if condition_velocity5:
        return 'WAIT WAIT'


print(check(x1, x2, v1, v2))
