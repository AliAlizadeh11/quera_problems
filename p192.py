t = int(input())

def prepare_word(n : int, w : int, text : str) -> str:
    result = list()
    text = list(text)
    w = int(w)
    for _ in range(n):
        answer = "".join(text[:w+1])
        answer.strip()
        len_answer = len(answer)
        
        if len_answer < w:
            count = w - len_answer
            add_space = count * " "
            final_answer = "|" + answer + add_space + "|"
            
        else:
            final_answer = "|" + answer + "|"
            
        result.append(final_answer)
        
        del text[:w+1]
    
    return result

result = list()
for i in range(t):
    n, w = list(map(int, input().split()))
    text = input()
    result.append(prepare_word(n, w, text))

for i in range(len(result)):
    print(result[i])
