n, t = list(map(str, input().split()))
passwords = list()

for _ in range(int(n)):
    pass_ = input()
    passwords.append(pass_)

def invalidate_password(t):
    t = set(list(t))
    return t

print(invalidate_password(t))

def check_password(t, passwords):
    for item in passwords:
        item = set(list(item))
        item.intersection_update(t)
        