n = int(input())
k = int(input())
p = input()

password = list()
for i in range(len(p)):
    password.append(p[i])

for _ in range(k):
    step1 = list(password[-1])
    step2 = password[0:len(password)-1]
    step3 = step1 + step2

    for j in range(len(password)):
        if ord(step3[j]) == 122:
            step3[j] = 'a'
        else:
            step3[j] = chr(ord(step3[j]) + 1)
    
    password = step3

print("".join(step3))