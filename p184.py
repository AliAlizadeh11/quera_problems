def compress(text: str) -> str:
    count = 0
    result = list()
    for i in range(len(text)):
        while text[i] == text[i + 1]:
            count += 1
            
        result.append(str(text[i]) + str(count))
            
        if text[i] != text[i + 1]:
            result.append(text[i])
        
        count = 0
        
    return result

print(compress("hhpwwwBbTTTTnnP"))
