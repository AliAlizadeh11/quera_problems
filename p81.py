def div(n):
    for i in range(1, int(n / 2) + 1):
        if n % i == 0:
            yield i
    yield n