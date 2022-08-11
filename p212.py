n = int(input())
road = list(map(int,input().split()))

def check_road(road):
    for i in range(len(road)):
        if i == int(len(road))-1:
            break
        
        elif road.index(road[i]) == 0:
            continue

        elif road[i] > road[i+1] and road[i] > road[i-1]:
            return 'Ey baba :('
            
    
    return 'Bah Bah! Ajab jooji!'

print(check_road(road))