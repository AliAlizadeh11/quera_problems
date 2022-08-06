n = int(input())
periods = list()

for _ in range(n):
    period = list(map(int , input().split()))
    periods.append(period)

def remove_covered_periods(intervals : list) -> int:
    intervals.sort(key=lambda i : (i[0], -i[1]))
    
    res = [intervals[0]]
    for l, r in intervals[1:]:
        preL, preR = res[-1]
        
        if preL <= l and preR>= r:
            continue
        res.append([l, r])
        
    return res

print(remove_covered_periods(periods))
