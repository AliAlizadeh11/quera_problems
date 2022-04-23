n, k, m, x, y = input().split()
l1 = [int(m)]
for i in range(int(n)):
    a = (int(x) * int(l1[i]) + int(y)) % ((10**9) + 7)
    l1.append(a)
l1.sort()
print(l1[int(k) - 1])