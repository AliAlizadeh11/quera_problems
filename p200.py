import collections
N = int(input())
colors = list(map(str, input().split()))

def calculate(colors):
    result = dict()
    count_ = dict(collections.Counter(colors))
    min_value = count_[min(count_, key=count_.get)]

    for i, j in count_.items():
        if j == min_value:
            result[i] = j

    return min(result.keys())

print(calculate(colors))
