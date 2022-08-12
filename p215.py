n, m, k = list(map(int, input().split()))
keyboard = [[1 for _ in range(m)] for _ in range(n)]

if k > 0:
    for _ in range(k):
        r, c = list(map(int, input().split()))
        keyboard[r-1][c-1] -= 1

def check(k : int, keyboard : list) -> int:
    if k == 0:
        return f"1\n1 1"
    
    impossible = False
    for item in keyboard:
        if item.count(1) == 0:
            continue
        
        elif item.count(1) != 0:
            impossible = True
            break
    
    if impossible == False:
        return -1
        
    elif k%2 != 0:
        return 0
    
    elif k%2 == 0:
        for item1 in keyboard:
            for item2 in item1:
                if item2 == 1:
                    return f"1\n{keyboard.index(item1) + 1} {item1.index(item2) + 1}"
        else:
            return -1
        
                
print(check(k, keyboard))
