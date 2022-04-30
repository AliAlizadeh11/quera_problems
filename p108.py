n = int(input())
count = 0

for i in range(1, n+1):
    if '0' in str(i) or '1' in str(i):
        a = str(i).count('0')
        b = str(i).count('1')
        if a + b == len(str(i)):
            count += 1
            
print(count)
