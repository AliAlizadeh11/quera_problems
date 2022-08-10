n, m = list(map(int, input().split()))

first_plate = list()
for item in range(n):
    plate = input()
    first_plate.append(plate)

second_plate = list()
for item in range(n):
    plate = input()
    second_plate.append(plate)
    

def count_meat(plates : list) -> int :
    result = 0
    
    for item in plates:
        meet = item.count('*')
        result +=meet
    
    return result

print(f"{count_meat(first_plate)} {count_meat(second_plate)}")