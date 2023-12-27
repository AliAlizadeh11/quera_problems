n = int(input())

def check(n):
    dp = [1, 1]
    for i in range(2, n+1):
        dp.append(dp[i-1] + dp[i-2])
    
    return dp[n-1]

print(check(n))