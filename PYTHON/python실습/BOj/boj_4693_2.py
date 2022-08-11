import sys
sys.stdin = open("input.txt")
sys.setrecursionlimit(10000)

def bfs(x, y):

    dx = [-1, -1, 0, 1, 1, 1, 0, -1]
    dy = [0, 1, 1, 1, 0, -1, -1, -1,] # 8개의 방향 
    visited[x][y] = 1 
    stack = [(x,y)]
    while stack:
        hx, hy = stack.pop()
        for i in range(8):
            nx = hx + dx[i]
            ny = hy + dy[i]
            if  -1 < nx < h and  -1 < ny < w:
                if list_[nx][ny] == 1 and visited[nx][ny] == 0:
                    visited[nx][ny] = 1
                    stack.append((nx,ny))




while True:
    w, h =map(int,input().split())
    visited = [[0]*w for _ in range(h)]
    if w == 0 and h == 0:
        break
    list_ = []
    cnt  = 0
    for _ in range(h):
        list_.append(list(map(int,input().split())))
    for i in range(h):
        for j in range(w):
            if list_[i][j] == 1:
                bfs(i, j)
                cnt += 1
    print(cnt)