n, a, b = list(map(int, input().split()))


def solution (a, b, n):
    i = 0
    while i * a <= n:
        if (n - (i * a)) % b == 0:
            return(f'{i} {int((n - (i * a)) / b)}')
        i = i + 1
    else:
        return -1
    
print(solution(a, b, n))