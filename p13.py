n = int(input())
l = []
for j in range(n):
    m = str(input())
    l.append(m)
i = 0
while i+1 != len(l):
    if n <= 2:
        a = f"{l[i]} to {l[i+1]}: ke ba in dar agar dar bande dar manand, dar manand."
        b = f"{l[i+1]} to {l[i]}: dar manand?"
        c = f"{l[i]} to {l[i+1]}: dar manand."
        print(a)
        print(b)
        print(c)
        i += 1
    elif n >= 3:
        a = f"{l[i]} to {l[i+1]}: ke ba in dar agar dar bande dar manand, dar manand."
        b = f"{l[i+1]} to {l[i]}: dar manand?"
        c = f"{l[i]} to {l[i+1]}: dar manand."
        d = f"{l[i+1]} to {l[i]}: dar manand?"
        e = f"{l[i+1]} to {l[i]}: dar manand?"
        print(a)
        print(b)
        print(c)
        i += 1
