x1 = int(input())
y1 = input().split()

x2 = int(input())
y2 = input().split()

x3 = int(input())
y3 = input().split()

a = set(y1 + y2 + y3)
b = {'shanbe', '1shanbe', '2shanbe', '3shanbe', '4shanbe', '5shanbe', 'jome'}
result = b.difference(a)
print(len(result))
