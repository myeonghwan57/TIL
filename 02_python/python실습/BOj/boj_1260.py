from collections import deque


n, m, v = map(int,input().split())
# 인접리스트 
graph = [[] for _ in range(n+1)]
# 방문  
visited_dfs = [False] * (n+1)
visited_bfs = [False] * (n+1)
for _ in range(m):
    # 연결
    x, y = map(int,input().split())
    graph[x].append(y)
    graph[y].append(x)

for i in range(len(graph)):
    graph[i].sort()

def dfs(v):
    print(v,end=' ')
    visited_dfs[v] = True
    for i in graph[v]:
        if visited_dfs[i] == False:
            dfs(i)

def bfs(v):
    q = deque([v])
    visited_bfs[v] = True
    while q:
        now = q.popleft()
        print(now,end=' ')
        for i in graph[now]:
            if not visited_bfs[i]:
                q.append(i)
                visited_bfs[i]=True

 
    

dfs(v)
print()
bfs(v)

