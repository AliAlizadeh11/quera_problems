import string
def IsPalindrome(s):
    for c in string.punctuation:
        s = s.replace(c, "").strip().lower()
    if len(s) < 2 or s[0] == s[-1] and IsPalindrome(s[1:-1]):
        return True
    else:
        return False
s = input()
if IsPalindrome(s):
    print('YES')
else:
    print('NO')