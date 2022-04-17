n, k = input().split()
n = int(n)
k = int(k)
sum_a = 0
for i in range(n):
    a = int(input())
    sum_a += a
if sum_a >= k:
    print('YES')
else:
    print('NO')
    