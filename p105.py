k = int(input())
password = str(input())
z = 0
for i in range(k):
    a = str(input())
    if a.find(password[i]) <= 4:
        z += a.find(password[i])
    else:
        z += (9-a.find(password[i]))
print(z)