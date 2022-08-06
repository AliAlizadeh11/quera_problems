n, t = list(map(str, input().split()))
discount_codes = list()

for _ in range(int(n)):
    discount_code = input()
    discount_codes.append(discount_code)

def check_discount_codes(discount_codes, t):
    result = list()
    for item in discount_codes:
        new_discount_code = set(list(item))
        len_t = len(t)
        
        if len(new_discount_code.intersection(set(t))) == len_t:
            result.append('Yes')
        
        else:
            result.append('No')
    
    return result
    
total = check_discount_codes(discount_codes, t)
for _ in total:
    print(_)
