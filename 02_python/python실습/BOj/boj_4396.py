n = int(input())
m = 0
dx = [0, 1, 1, 1, 0, -1, -1, -1]
dy = [1, 1, 0, -1, -1, -1, 0, 1]
map = [input() for _ in range(n)]
check = [input() for _ in range(n)]
result = ['.' for _ in range(n)]
flag = 0
for i in range(n):
    for j in range(n):
        if check[i][j] == 'x':
            cnt = 0
            for d in range(8):
                nx = i + dx[d]
                ny = j + dy[d]
                if 0 < nx < n-1 and 0 < ny < n-1:
                    map[nx][ny] == '*'
                    cnt += 1 
            result[i][j] = str(cnt) 
            if map[i][j] == '*':
                flag = 1
if flag == 1 :
    for i in range(n):
        for j in range(n):
            if map[i][j] == '*':
                result[i][j] = '*'
for i in result:
    print(''.join(i))
