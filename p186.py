n, m = list(map(int, input().split()))
l = ""
for item in range(n):
    a = input()
    l = l + a
    
print(l.count("*"))
