a,b,l= input().split(" ")
a = int(a)
b = int(b)
l = int(l)
time = 0
count = 0
while True:
    time += a
    count += 1
    time += b
    count += 1
    if count == l:
        break
print(time)

    
    
    