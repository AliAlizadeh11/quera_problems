def best_sum(target_sum, numbers, dp = list()):
    if target_sum in dp:
        return dp[target_sum]
    
    if target_sum == 0:
        return []
    
    if target_sum < 0:
        return None
    
    shortest_combinations = None
    
    for num in numbers:
        remaining = target_sum - num
        remainder_combinations = best_sum(remaining, numbers, dp)
        
        if remainder_combinations != None:
            combination = remainder_combinations.append(num)
            
            if shortest_combinations == None or len(combination) < len(shortest_combinations):
                shortest_combinations = combination
                
    dp[target_sum] = shortest_combinations
    return shortest_combinations

best_sum(8, [2, 3, 5])
