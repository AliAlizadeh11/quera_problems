k = int(input())
password = input()
count_total = 0
for j in range(k):
    l = input()
    l1 = l
    l2 = l[::-1]
    count1 = 0
    a = password[j]
    b = str(l1.index(a))
    c = str(l2.index(a))
    calculate1 = abs(int(b))
    calculate2 = abs(int(c) + 1)
    if calculate1 < calculate2:
        count1 += calculate1
    elif calculate1 > calculate2:
        count1 += calculate2
    count_total += count1
print(count_total)
