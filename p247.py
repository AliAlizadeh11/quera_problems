def can_construct(target:str, word_bank:list, dp = dict()) -> bool:
    if target in dp:
        return dp[target]
    
    if target == "":
        return True
    
    for word in word_bank:
        if target.find(word) == 0:
            suffix = target[len(word):]
            if can_construct(suffix, word_bank, dp) == True:
                dp[target] = True
                return True
            
    dp[target] = False
    return False

print(can_construct("abcdef", ["ab", "abc", "cd", "def", "abcd"]))
print(can_construct("skateboard", ["bo", "rd", "ate", "t", "ska", "sk", "boar"]))
# string = ""
# for _ in range(10000):
#     string +='a'
# print(can_construct(string, ["a", "abc", "cd", "def", "abcd"]))