x = int(input())
l1 = input()
l2 = input()
count = 0
for i in range(len(l1)):
    if l1[i] == l2[i]:
        continue
    else:
        count += 1
print(count)