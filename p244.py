n, m = list(map(int, input().split()))

def grid_traveler(m, n, dp = dict()):
    item = str(m) +',' + str(n)
    
    if item in dp:
        return dp[item]
    
    if m == 1 and n == 1:
        return 1
    
    if m == 0 or n == 0:
        return 0
    
    dp[item] = grid_traveler(m-1, n) + grid_traveler(m, n-1)
    return dp[item]

print(grid_traveler(m, n))
