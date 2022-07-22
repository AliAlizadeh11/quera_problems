import numpy as np
m = int(input())
mat = []
for i in range(m):
    mat.append(list(map(int, input().split())))


def check_col(col, row):
    for row_ in range(row + 1, m):
        if mat[col][row_] == 1 and not is_checked[col][row_]:
            sum_ += 1
            is_checked[col][row_] = True
            check_row(col, row_)
        else:
            break

    for row_ in range(row - 1, -1, -1):
        if mat[col][row_] == 1 and not is_checked[col][row_]:
            sum_ += 1
            is_checked[col][row_] = True
            check_row(col, row_)
        else:
            break


def check_row(col, row):
    for col_ in range(col + 1, m):
        if mat[col_][row] == 1 and not is_checked[col_][row]:
            sum_ += 1
            is_checked[col_][row] = True
            check_col(col_, row)
        else:
            break

    for col_ in range(col - 1, -1, -1):
        if mat[col_][row] == 1 and not is_checked[col_][row]:
            sum_ += 1
            is_checked[col_][row] = True
            check_col(col_, row)
        else:
            break


def check(col, row):
    sum_ = 0
    if mat[col][row] == 0 or is_checked[col][row] == True:
        return 0
    else:
        sum_ += 1
        is_checked[col][row] = True

    check_col(col, row)
    check_row(col, row)

    return sum_


col = 0
row = 0
mat = np.array(mat)
is_checked = np.zeros((m, m), dtype=bool)
max_sum = 0

for col in range(m):
    for row in range(m):
        sum_cr = check(col, row)

        if sum_cr > max_sum:
            max_sum = sum_cr

print(max_sum)
