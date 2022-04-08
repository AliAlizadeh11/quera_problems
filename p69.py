s = input()
l = []
for i in range(len(s)):
    l.append(s[i])
    if s[i] == '=':
        if l.index(s[i]) > 0:
            l.pop()
            l.pop()
        else:
            l.pop()
result = "".join(l)
print(result)