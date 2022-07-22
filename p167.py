import random

l = list()
for i in range(1_000_000):
    n = 1
    while random.randint(1, 6) != 6:
        n += 1
    l.append(n)

print(sum(l)/len(l))
