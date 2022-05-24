s = input()
l = []
for i in range(len(s)):
    l.append(s[i])    
a1 = l.count('R') >= 3
a2 = l.count('Y') >= 2 and s.count('R') >= 2
a3 = l.count('G') == 0

if a1 or a2 or a3:
    print('nakhor lite')
else:
    print('rahat baash')
