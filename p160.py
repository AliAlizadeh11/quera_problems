n, k = list(map(int, input().split()))
result = 0
for i in range(n):
    value1, value2 = list(map(int, input().split()))
    compare = value2 - value1 
    if compare >= 0:
        result += compare
    elif compare < 0:
        pass

if result == 0:
    print(0)
else:
    print(k + result)
