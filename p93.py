n, A,B = list(map(int, input().split()))

reference = []
for i in range(n):
    reference.append(list(map(int, input().split())))

first_path_A = [A]
first_path_B = [B]
second_path_A = [A]
second_path_B = [B]

find = False
for length in range(n):
    if reference[first_path_A[length]][2] != reference[first_path_B[length]][2] \
    or reference[second_path_A[length]][2] != reference[second_path_B[length]][2]:
        find = True
        break
    
    first_path_A.append(reference[first_path_A[length]][0])
    first_path_B.append(reference[first_path_B[length]][0])
    second_path_A.append(reference[second_path_A[length]][1])
    second_path_B.append(reference[second_path_B[length]][1])
    

if find:
    print(length)
else:
    print('indistinguishable')