n, k = input().split()
n = int(n)
k = int(k)
l = input().split()
l = [int(x) for x in l]
calculate1 = n * k
calculate2 = sum(l)
result = int((calculate1 - calculate2) / k)
print(result)
