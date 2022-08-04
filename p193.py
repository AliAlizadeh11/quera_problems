n, k = list(map(float, input().split()))

def show_calculated(n, k):
    if n%k == 0:
        return int(n/k)

    elif n%k != 0:
        return int(n)
    
print(show_calculated(n, k))
