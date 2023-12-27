def can_sum(target, numbers, dp = dict()):
    if target in dp:
        return dp[target]
    
    if target == 0:
        return []
    
    if target < 0:
        return None
    
    for number in numbers:
        remainder = target - number
        result = can_sum(remainder, numbers)
        
        if result != None:
            temp = result + [number]
            dp[result] = temp
            return result
        
    dp[target] = None
    return None

print(can_sum(7, [2, 3, 4]))