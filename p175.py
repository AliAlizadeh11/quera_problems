n, q = list(map(int, input().split()))
queues = [[] for _ in range(n)]
result = list()

for i in range(q):
    input_ = list(map(int, input().split()))
    first_input = input_[0]
    
    if first_input == 1:
        for j in queues:
            j.append(input_[1])
            
    elif first_input == 2:
        number = input_[1] - 1
        item_delete = input_[2]
        
        result.append(sum(queues[number][0:item_delete]))
        queues[number] = queues[number][item_delete:]
        
for _ in result:
    print(_)