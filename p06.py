def comb(n, k):
    """calculate comb(tarkibiat)"""
    answer = 1
    for i in  range(n - k + 1, n + 1):
        answer *= i
    for i in range(1, k + 1):
        answer /= i
    return answer