N = int(input())
s = input()

k1 = '331122'
n1 = '123'
sh1 = '2123'
k2 = (N // 6) + 1
n2 = (N // 3) + 1
sh2 = (N // 4) + 1

k3 = k1 * k2
n3 = n1 * n2 
sh3 = sh1 * sh2

k4 = list()
for i in range(len(k3)):
    k4.append(k3[i])

n4 = list()
for i in range(len(n3)):
    n4.append(n3[i])

sh4 = list()
for i in range(len(sh3)):
    sh4.append(sh3[i])
    

total = {
    'keyvoon':0,
    'nezam': 0,
    'shir farhad':0,
}

for i in range(len(s)):
    if k4[i] == s[i]:
        total['keyvoon'] += 1
    
    if n4[i] == s[i]:
        total['nezam'] += 1
    
    if sh4[i] == s[i]:
        total['shir farhad'] += 1

result1 = max(total.values())
print(result1)
result2 = list()
for i, j in total.items():
    if j == result1:
        result2.append(i)

result2.sort()
for i in range(len(result2)):
    print(result2[i])



    