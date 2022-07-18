def decimal_to_binary(n):
    return bin(n).replace("0b", "")

n = int(input())

result = str(decimal_to_binary(n))
zero_count = result.count('0')
one_count = result.count('1')

if one_count > zero_count:
    print('NO')
elif one_count < zero_count:
    print('YES')
