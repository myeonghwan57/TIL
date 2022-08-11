import sys
sys.stdin = open("input.txt")
sys.setrecursionlimit(10000)

def dfs(x, y):
    dx = [-1, -1, 0, 1, 1, 1, 0, -1]
    dy = [0, 1, 1, 1, 0, -1, -1, -1,]
    list_[x][y] = 0
    for i in range(8):
        nx = x + dx[i]
        ny = y + dy[i]
        if -1 < nx < h and  -1 < ny < w and list_[nx][ny] == 1:
            dfs(nx, ny) 
while True:
    w, h =map(int,input().split())
    if w == 0 and h == 0:
        break
    list_ = []
    cnt = 0
    for _ in range(h):
        list_.append(list(map(int,input().split())))
    for i in range(h):
        for j in range(w):
            if list_[i][j] == 1:
                dfs(i, j)
                cnt += 1
    print(cnt)
