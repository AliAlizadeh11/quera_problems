from itertools import permutations

x = input()

l = list(permutations(x))
total = list()
for i in l:
    item = "".join(i)
    total.append(int(item))


def calculate(total : list) -> int:
    total = list(set(total))
    total.sort()
    index_number = total.index(int(x))
    
    if index_number == len(total) - 1 :
        return 0
    
    else:
        return total[index_number + 1]

print(calculate(total))