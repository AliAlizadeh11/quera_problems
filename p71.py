import re
#A + B = C
def solve(s):
    s = str(s)
    a = s.index('+')
    b = s.index('=')
    c = s.index('#')
    
    if a > c:
        x = s[:a-1]
        x.strip()
        y = int(s[b+1:].strip()) - int(s[a+1:b-1:].strip()) 
    elif a < c and c < b:
        x = s[a+1:b-1]
        x.strip()
        y = int(s[b+1:].strip()) - int(s[:a-1].strip())
    else:
        x = s[b+1:]
        x.strip()
        y = int(s[:a+1].strip()) + int(s[a+1:b-1:].strip())
        
    t1 = x[:c]
    t1 = str(t1)
    t2 = x[c+1:]
    t2 = str(t2)
    
    if re.match(r'^t1.*t2$', str(y)):
        return y
    else:
        return '-1'
s = input()
solve(s)