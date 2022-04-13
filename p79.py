def calc(a):
    a = sorted(a)
    average_result = sum(a) / len(a)
    maximum_result = max(a)
    
    if len(a) % 2 != 0:
        i1 = (len(a) // 2)
        median_result = int(a[i1])
    else:
        j1 = int((len(a) // 2) - 1)
        j2 = int(len(a) // 2)
        median_result = (a[j1] + a[j2]) / 2
    
    total_result = (average_result, median_result, maximum_result)
    return total_result