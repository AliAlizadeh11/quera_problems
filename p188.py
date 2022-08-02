n = int(input())
exam_key = input()
k = int(input())

answers = list()
for _ in range(n*k):
    input_ = input()
    answers.append(input_)

def convert_key(exam_key : str) -> str :
    result = ""
    convert_dict = {'A':1, 'B':2, 'C':3, 'D':4}
    for item in exam_key:
        result += str(convert_dict[item])
    
    return result

def grade_calculate(t : int, f : int) -> float :
    result = 3 * t - f
    return result

def convert_answer(answers : list) -> int:
    total = list()
    
    for item in answers:
        result = ""
        answer_count = str(item).count("#")

        if answer_count == 1:
            answer_index = str(item).index('#')
            result += str(int(answer_index)+1)
            total.append(result)
        
        else:
            total.append('-1')
            
    
    return total

def total_value(result : list) -> list:
    for item in result:
        check_item = grade_calculate(item)
        print(check_item)


print(convert_key(exam_key))
print(grade_calculate(10, 4))
print(convert_answer(answers))
print(total_value())