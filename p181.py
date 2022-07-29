from itertools import count


n = list(map(int, input().split()))

count = 0
for i in n:
    if i >= 80:
        count += 1
    else:
        continue

if count >= 3:
    print("Mamma mia!")
elif 1 <= count <= 2:
    print("Mamma mia!!")
else:
    print("Mamma mia!!!")