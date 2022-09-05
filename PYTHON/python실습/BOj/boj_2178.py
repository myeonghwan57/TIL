N, M = map(int,input().split())
map = [list(map(int, input().split())) for _ in range(N)]
# 1 0 1 1 1 1
# 1 0 1 0 1 0
# 1 0 1 0 1 1
# 1 1 1 0 1 1 

dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]

