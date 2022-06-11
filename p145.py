s = input()
l1 = list()

for i in range(len(s)):
    Xi = int(s.count(s[i].lower()) + s.count(s[i].upper()))
    if ord(s[i]) >= 65 and ord(s[i]) <= 90:
        Ai = int(ord(s[i]) - 65)
    if ord(s[i]) >= 97 and ord(s[i]) <= 122:
        Ai = int(ord(s[i]) - 97)
        
    y = (Xi * Ai + 1) % 26

    if ord(s[i]) >= 65 and ord(s[i]) <= 90:
        l1.append(chr(y+65))


    if ord(s[i]) >= 97 and ord(s[i]) <= 122:
        l1.append(chr(y+97))

print(''.join(l1))