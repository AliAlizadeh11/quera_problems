n, m = list(map(int, input().split()))
def grid_traveler(n, m):
    if m ==1 and n ==1:
        return 1
    elif m == 0 or n == 0:
        return 0
    
    return grid_traveler(m-1, n) + grid_traveler(m, n-1)

print(grid_traveler(n, m))