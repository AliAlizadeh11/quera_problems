text = input()

def check(text : str) -> str:
    total = list()
    count = 1
    
    for i in range(1, len(text)):
        if text[i-1] == text[i]:
            count += 1
            
        else:
            total.append(count)
            count = 1
    else:
        total.append(count)
        
    return total

def final(total : list) -> str:
    for item in total:
        if item%2 != 0:
            return 'bad '

    else:
        return 'khoob'

print(final((check(text))))
