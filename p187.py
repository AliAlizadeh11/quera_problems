password1 = input().split()
password2 = input().split()
password1 = "".join(password1)
password2 = "".join(password2)

reference1 = [password1[1:4], password1[0:3], password1[4] + password1[0:2], password1[3:] + password1[0], password1[2:]]
reference2 = [password2[1:4], password2[0:3], password2[4] + password2[0:2], password2[3:] + password2[0], password2[2:]]

def calculate():
    for item1 in reference1:
        for item2 in reference2:
            answer1 = int(item1[0]) + int(item2[0])
            answer2 = int(item1[1]) + int(item2[1])
            answer3 = int(item1[2]) + int(item2[2])
            
            total = [answer1, answer2, answer3]
            
            for item3 in total:
                result = ""
                if len(str(item3)) == 2:
                    result += str(item3)[-1]
                else:
                    result += str(item3)
                
                if int(result)%6 == 0:
                    return "Boro joloo :)"
                
                else:
                    continue

    return "Gir oftadi :("
    
print(calculate())