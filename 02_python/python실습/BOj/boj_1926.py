n,m = map(int,input().split())
# 그림이라는 것은 1로 연결된것을 한그림이라도 정의 
# 대각선은 떨어진 그림 
# 그림의 넓이는 그림에 포함된 1의 개수 
dx = [1,-1,0,0]
dy = [0,0,1,-1]
# 도화지 입력
map = [list(map(int,input())) for _ in range(n)]
# 그림 넓이 카운트
def dfs(x,y):
    map[x][y] = 0
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if -1<nx<n and -1<ny<n and map[nx][ny] == 1:
            dfs(nx,ny)  
cnt = 0
for i in range(n):
    for j in range(m):
        if map[i][j]==1:
            cnt = 1
            dfs(i,j)
            

