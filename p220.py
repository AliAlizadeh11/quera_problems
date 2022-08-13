a, b, c, d, m = list(map(int,input().split()))

def calculate1(a, c, m):
    result1 = list()
    first_price = a
    second_price = a
    for _ in range(m):
        second_price += c
    
    result1.append(second_price)
    result1.append((second_price-first_price)*m)
    return result1

def calculate2(b, d, m):
    result2 = list()
    first_price = b
    second_price = b
    
    for _ in range(m):
        second_price += d
    
    result2.append(second_price)
    result2.append((second_price-first_price)*m)
    return result2

def compare(result1, result2):
    if result1[0] > result2[0] and result1[1] > result2[1]:
        return 'Eyval baba!'
    
    elif result2[0] > result1[0] and result2[1] > result1[1]:
        return 'Eyval baba!'
    
    else:
        return 'Naaa, eshtebahe!'

print(compare(calculate1(a,c,m), calculate2(b, d, m)))
