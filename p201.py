a, b, x = list(map(int, input().split()))

def divisorGenerator(n : int) -> int:
    if n == 1:
        return 1
    
    else:
        for i in range(1,int(n/2)+1):
            if n%i == 0:
                yield i
                
            yield n
        
def divisor_reference(a : int) -> int:
    if a == 1:
        return [1]
    number = list()
    for item in divisorGenerator(a):
        number.append(item)
    
    return list(set(number))


def final(a : int, b : int, x : int, first_l : list, second_l : list) -> int:
    
    if a == b == x == 2:
        return 1
    
    answer = 0
    for item1 in first_l:
        for item2 in second_l:
            if item1 + item2 <= x:
                answer += 1
    
    return answer

print(final(a, b, x, divisor_reference(a), divisor_reference(b)))
