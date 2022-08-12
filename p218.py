n, m = list(map(int,input().split()))

maps1 = list()
for _ in range(n):
    map_ = input()
    maps1.append(map_)

def create_map2(maps1):
    maps2 = list()
    result = ""
    for item1 in range(len(maps1)):
        for item2 in range(len(maps1[item1])):
            result +=maps1[item2][item1]
        maps2.append(result)
        result = ""

    return maps2

def calculate1(maps1):
    result = 0
    new_l = list()
    for item in maps1:
        answer = item.split('-')
        new_l.extend(answer)
    for item in new_l:
        if item != "":
            result += 1
    
    return result

def calculate2(maps2):
    result = 0
    new_l = list()
    for item in maps2:
        answer = item.split('|')
        new_l.extend(answer)
    for item in new_l:
        if item != "":
            result += 1
    
    return result

print(calculate1(maps1) + calculate2(create_map2(maps1)))
