k = int(input())

def get_divisors(m):
    result = 0
    for i in range(1, int(m / 2) + 1):
        if m % i == 0:
            result += 1
            
    return result+1

def series_sum(n, k):
    sum = 0
    for i in range(1, n + 1):
        sum = i * (i + 1) / 2
        if get_divisors(sum) == k:
            return int(sum)


print(series_sum(1000, k))