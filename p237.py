def check(blood):
    d, m, c = blood[0], blood[1], blood[2]
    parent_blood = d + m
    parent_rh = parent_blood.count('-')
    
    if len(c) == 2:
        child_blood = c[0]
        child_rh = c[1]
        
    elif len(c) == 3:
        child_blood = c[:2]
        child_rh = c[2]
        
    if child_blood == 'O':
        if child_rh == '-' and parent_rh == 2:
            return 'invalid'
        
        return 'valid'
    
    elif child_blood == 'A':
        if 'A' in parent_blood and parent_rh != 2:
            return 'valid'
        
        return 'invalid'
    
    elif child_blood == 'B':
        if 'B' in parent_blood and parent_rh != 2:
            return 'valid'
        
        return 'invalid'
    
    elif child_blood == 'AB':
        if 'A' in parent_blood and 'B' in parent_blood and parent_rh != 2:
            return 'valid'
        
        return 'invalid'

t = int(input())
result = list()

for i in range(t):
    blood = list(map(str, input().split()))
    result.append(check(blood))

for item in result:
    print(item)