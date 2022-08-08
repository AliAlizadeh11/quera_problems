L, R = list(map(int, input().split()))

def text_inverse(text):
    result = ""
    
    for item in text:
        if item == '0':
            result += '1'
        
        elif item == '1':
            result += '0'
            
    return result

def text_edit(L, R):
    result = '1'
    text = '1'
    
    for _ in range(R):
        if len(result) > R+1 :
            break
        
        add_text = text_inverse(text)
        result += add_text
        text = result
    
    return result[L-1:R]

print(text_edit(L, R))
