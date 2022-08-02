t, w = list(map(int, input().split()))
result = 0
for i in range(w):
    denominator = 2**i
    result += 1/denominator

final = t/result
print('{:.4f}'.format(final))
