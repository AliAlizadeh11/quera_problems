n, m , k = list(map(int, input().split()))
wall = [['' for y in range(m)] for x in range(n)]

for i in range(1,k+1):
    ri, ci, ki= list(map(int, input().split()))
    for j in range(ri-1, ri+ki-1):
        for z in range(ci-1, ci+ki-1):
            wall[j][z] = wall[j][z] + str(i)

result = list()
for i in range(len(wall)):
    for j in range(len(wall[i])):
        if not wall[i][j] in result:
            result.append(wall[i][j])

print(len(result)-1)