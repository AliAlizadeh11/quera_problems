n, x = list(map(str, input().split()))

def change_glasses(glass : list) -> list :
    
    for _ in range(int(n)):
        position1, position2 = list(map(str, input().split()))
        
        p1 = glass.index(position1)
        p2 = glass.index(position2)
        
        glass[p1] = position2
        glass[p2] = position1
        
    return glass
    
def answer_glasses(glass_list : list, x : str) -> str :
    final_position = glass_list.index(x)
    
    if final_position == 0 :
        return "L"
    
    elif final_position == 1 :
        return "M"
    
    elif final_position == 2 :
        return "R"

print(answer_glasses(change_glasses(['L', 'M', 'R']), x))
