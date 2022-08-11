n = int(input())

def check(n : int) -> float:
    result = 0
    for i in range(n+1):
        num = (min(i, n-i))
        result += num

    return result / (n+1)

number = check(n)
print('{:.5f}'.format(number))