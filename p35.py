n = int(input())
if n%2 == 0:
    print(int((n/2 + 1) ** 2))
elif n%2 == 1:
    print(int(((n+1)/2)) * int(((n+1)/2) + 1))