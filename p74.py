n = int(input())
l1 = []
for i in range(n):
    a = int(input())
    l1.append(a)
# for item in range(n):

def find_total_possible(n):
    x = [i for i in range(n + 1)]
    y = [i + 1 for i in range(n + 1)]
    z = list(zip(x,y))
    return z

find_total_possible(5)