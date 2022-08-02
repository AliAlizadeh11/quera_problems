words = list()
for _ in range(5):
    word = input()
    words.append(word)
    
def check_word(words):
    result = list()
    for i, item in enumerate(words):
        if 'MOLANA' in item or 'HAFEZ' in item:
            result.append(i+1)
            
    return result

def answer(result):
    if len(result) == 0:
        print('NOT FOUND!')

    else:
        print(*result)

answer(check_word(words))
