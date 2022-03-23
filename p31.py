n = input().lower()
result = 1
if len(n) == 6:
    if 'a' in n:
        result *= 2 ** (n.count('a'))
    if 'e' in n:
        result *= 2 ** (n.count('e'))
    if 'i' in n:
        result *= 2 ** (n.count('i'))
    if 'o' in n:
        result *= 2 ** (n.count('o'))
    if 'u' in n:
        result *= 2 ** (n.count('u'))
print(result)
        