L = []
while True:
    a = int(input())
    if a == 0:
        break
    L.insert(0, a)

for j in range(len(L)):
    print(L[j])