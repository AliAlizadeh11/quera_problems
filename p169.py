n, q = list(map(int, input().split()))
road1 = list(map(int, input().split()))
road2 = road1.copy()
l1 = list()

for i in range(q):
    a, b = list(map(int, input().split()))
    c = road2[a-1:b]
    for j in c:
        if j == 0 or j == 1:
            pass