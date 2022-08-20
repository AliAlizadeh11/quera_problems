T = int(input())
count = 0
l = list()
for _ in range(T):
    a = input()
    for i in range(len(a)):
        if a[i] in '13579':
            count += 1
        elif a[i] in 'aeiou':
            count += 1
    l.append(count)
    count = 0

for i in range(len(l)):
    print(l[i])