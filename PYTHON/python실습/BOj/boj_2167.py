#2차원 배열의 합
N, M = map(int,input().split())
matrix = []
for i in range(N):
    matrix.append(list(map(int,input().split())))
K = int(input())
for j in range(K):
    sum  = 0
    i, j, x, y = map(int,input().split())
    for a in range(i-1,x):
        for b in range(j-1,y):
            sum += matrix[a][b]
    print(sum)


