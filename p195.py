n = int(input())
w = list(map(int, input().split()))

def answer(w):
    max_ = max(w)
    return w.index(max_) + 1

print(answer(w))
