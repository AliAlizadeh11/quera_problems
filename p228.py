n, x = list(map(str, input().split()))

positions = {'L': 0, 'M' : 1, 'R' : 2,}

glass = ["", "", ""]

glass[positions[x]] += 'nokhod'


for i in range(int(n)):
    a, b = list(map(str, input().split()))
    if (a == 'L' and b == 'R') or (a == 'R' and b == 'L'):
        glass[positions[a]], glass[positions[b]] = glass[positions[b]],glass[positions[a]]
        
    elif (a == 'L' and b == 'M') or (a == 'M' and b == 'L'):
        glass[positions[a]], glass[positions[b]] = glass[positions[b]],glass[positions[a]]
        
    else:
        glass[positions[a]], glass[positions[b]] = glass[positions[b]],glass[positions[a]]

def final_result(glass):
    
    result = glass.index('nokhod')
    if result == 0:
        return('L')
    
    elif result == 1:
        return('M')
    
    else:
        return('R')

print(final_result(glass))