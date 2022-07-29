def check1(a, b):
    if a == b or a - b == 2:
        return True
    else:
        return False

def check2(a, b):
    if a%2 == 0 or b%2 == 0:
        return True
    else:
        return False

    
def show(result):
    for _ in result:
        print(_)

        
result = list()
t = int(input())
for i in range(t):
    a, b = list(map(int, input().split()))
    
    if check1(a, b) == True:
        if check2(a, b) == True:
            result.append(a+b)
            
        elif check2(a, b) == False:    
            result.append(a+b-1)
        
    elif check1(a, b) == False:
        result.append(-1)

for _ in result:        
    print(_)





        