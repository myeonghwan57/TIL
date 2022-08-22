N = 19 
point_list = [list(map(int, input().split())) for _ in range(N)]
dx = [1, 1, 0, -1]  # 하(↓), 우하(⬊), 우(➞), 우상(⬈)
dy = [0, 1, 1, 1]
for x in range(N):
    for y in range(N):
        if point_list[x][y] != 0:
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                cnt = 1
                if -1 < nx < 19 and -1 < ny < 19:
                    continue
                if point_list[x][y] == point_list[nx][ny]:
                    cnt += 1
                    
                