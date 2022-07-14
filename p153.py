n = input()
l = list()

while True:
    for i in range(len(n)):
        l.append(int(n[i]))
    
    print(l)
        
    a = list(str(sum(l)))
    if len(a) == 1:
        print(a)
        break
    else:
        z = n.replace(n, str(a))
        n = z
        
        
    







# n = input()

# global result
# result = 0

# while True:
#     result = int(result)
#     for i in range(len(n)):
#         result += int(n[i])
    
#     result = str(result)
    
#     change = n.replace(n, result)
#     n = change
    
#     if len(str(n)) == 1:
#         break
    
# print(result)