l, r = list(map(int, input().split()))
n = int(input())

total = list()
result = list()

for i in range(n):
    t1, t2 = list(map(int, input().split()))
    total.extend(range(t1, t2+1))

crime_time = list(range(l,r+1))

for i in crime_time:
    t3 = total.count(i)
    if t3 >= 1:
        result.append(t3)

print(result)
print(min(result), max(result))