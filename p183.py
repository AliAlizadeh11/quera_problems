n, k, s = list(map(float, input().split()))
def check(n, k, s):
    if n*k <= s:
        return "Kafie!"
    else:
        return "Na! yeki bayad bere sabzi bekhare"

print(check(n, k, s))