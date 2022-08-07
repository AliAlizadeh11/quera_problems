n, l = list(map(int, input().split()))

numbers = list()
distances = list()
for i in range(n):
    number = list(map(int, input().split()))
    distances.append(number[0])
    numbers.append(number)

def last_distances(l : int, numbers : list) -> int:
    last_distance = l - numbers[-1][0]
    
    return last_distance

last_distances(l, numbers)

def diff_consecutive_nums(distances : list) -> list:
    first = [distances[0]]
    result = [b-a for a, b in zip(distances[:-1], distances[1:])]
    final = first + result
    return final

def update_distance(numbers : list, distances : list) -> list:
    update_distances = diff_consecutive_nums(distances)
    for i in range(len(numbers)):
        numbers[i][0] = update_distances[i]

    return numbers

def calculate(data : list) -> int:
    count = 0
    time_travel = 0
    
    for item in data:
        d = item[0]
        r = item[1]
        g = item[2]
        
        time_travel += d
        red_waiting = r - d
        
        if red_waiting > 0:
            time_travel += red_waiting
    
        count += (d + r + g)
        
        
        
    


calculate(update_distance(numbers, distances))
