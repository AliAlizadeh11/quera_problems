n, m = map(int, input().split())
k = int(input())

my_map = []
for x in range(n):
    row, column = map(int, input().split())
    my_map.append([row, column])

print(my_map)