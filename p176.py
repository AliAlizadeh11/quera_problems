A = list()
n = int(input())
for _ in range(n):
    a = list(map(int, input().split()))
    A.append(a)


ans = 0
edges = [[] for i in range(1000)]
def Add_edge(u, v):
    global edges
    edges[u].append(v)
    edges[v].append(u)


def minTimeToColor(node, parent, arrival_time):
    global ans
    current_time = 0
    
    for x in edges[node]:
        if (x != parent):
            current_time += 1
            
            if (current_time == arrival_time):
                current_time += 1
                
            ans = max(ans, current_time)
            
            minTimeToColor(x, node, current_time)

    
for i in A:
    Add_edge(i[0], i[1])
    
minTimeToColor(1, -1, 0)
print(ans)

