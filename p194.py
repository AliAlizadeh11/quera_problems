number = input()
reference = {1:1,2:2,3:3,4:4,5:5, 6:6,7:7, 8:8, 9:9,'A':10, 'B':11, 'C':12, 'D':13, 'E':14, 'F':15}


def calculate(number : list) -> int :
    number = list(str(number))
    result = 0 
    for i, item in enumerate(number):
        if str(item).isdigit() == True and i == 0:
            add_ = int(item) * 16
            result += add_
            
        elif str(item).isdigit() == True and i != 0:
            result += int(item)
        
        elif str(item).isalpha() == True:
            result += reference[item]

    return result

def final():
    ans = "{:x}".format(calculate(number)+1)
    return ans.upper()

print(final())
