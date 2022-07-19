n = int(input())
m = input()
t, s = list(map(int, input().split()))


def decimal_to_binary(n):
    return bin(n).replace("0b", "")

def new_road(t, s):
    if t < s:
        road = list(filter(None, str(m[t-1:s]).split('P')))
    else:    
        road = list(filter(None, str(m[s-1:t]).split('P')))
    
    return road

def answer(road):
    final = [decimal_to_binary(len(i)).count('1') for i in road]
    return sum(final)

print(answer(new_road(t, s)))