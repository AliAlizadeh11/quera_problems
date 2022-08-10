n = int(input())
numbers = list(map(int, input().split()))

def calculate1(numbers):
    numbers.sort()
    len_numbers = int(len(numbers))
    numbers1 = numbers[:len_numbers//2]
    
    return numbers1

def calculate2(numbers):
    numbers.sort()
    len_numbers = int(len(numbers))
    numbers2 = numbers[len_numbers//2:]
    numbers2.reverse()
    
    return numbers2


def intersperse(seq, value):
    result = [value] * (2 * len(seq) - 1)
    result[::2] = seq
    return result


def final_answer(first_list : list, second_second_list : list) -> list:
    first_list = calculate1(numbers)
    second_list = intersperse(calculate2(numbers), "")
    index_l = 0
    for i in range(len(second_list)):
        if second_list[i] == "":
            second_list[i] += str(first_list[index_l])
            index_l += 1
            
    second_list = [str(i) for i in second_list]
    return " ".join(second_list)
        
print(final_answer(calculate1(numbers), intersperse(calculate2(numbers), "")))