n = int(input())
m = list(map(int, input().split()))
sum_ = sum(m)

if sum_ >= 0 and m[0] > 0 :
    print(m[0])
elif sum_ == 0 and m[0] < 0:
    print(0)
elif sum_ < 0 and m[0] > 0:
    print(m[0])
elif sum_ < 0 and m[0] < 0:
    print(0)