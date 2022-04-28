n, m = input().split()
n = int(n)
m = int(m)

for i in range(n):
    l1 = input().split()
    r1 = {l1[i]: l1[i + 1] for i in range(0, len(l1), 2)}
    l1.clear()

m1 = input().split()

l2 = []
for i in range(len(m1)):
    if m1[i] in r1.keys():
        l2.append(r1.values[i])
        l3.append("kachal!")
    else:
        l3.append("kachal!")

print(" ".join(l3))


def Convert(lst):
    res_dct = {lst[i]: lst[i + 1] for i in range(0, len(lst), 2)}
    return res_dct

# Driver code
lst = ['a', 1, 'b', 2, 'c', 3]
print(Convert(lst))
