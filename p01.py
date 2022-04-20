number_list = []
i = 0    
while i < 100:
    number = int(input())
    if number == 0:
        break
    number_list.insert(0, number)
for j in range(len(number_list)):
    print(number_list[j])