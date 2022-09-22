from collections import deque

N = int(input())
# 집 있는곳 입력.
_map = []
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
for _ in range(N):
    _map.append(list(map(int,input())))

def bfs (graph, x, y):
    
    q = deque((x,y))
    # 1인곳을 다시 방문하지 않게 0으로 바꿔줌.
    graph[x][y] = 0
    # 집이 있는곳이니까 count = 1 초기화 
    count = 1
    while q:
        x,y = q.popleft()
        
        for i in range(4):
           
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= N or ny < 0 or ny >= N:
                continue
            if graph[nx][ny] == 1:
                graph[nx][ny] = 0
                q.append((nx,ny))
                count += 1
    return count


# 단지 갯수
town = []
for i in range(N):
    for j in range(N):
        if _map[i][j] == 1:
            town.append(bfs(_map, i, j))

town.sort()
print(len(town))
for i in range(len(town)):
    print(town[i])
    

