#성지키기
n, m = map(int, input().split())
 
castle = []
 
for _ in range(n):
    castle.append(input())
 
cnt_r = 0
cnt_c = 0
 
for i in range(n):
    if "X" not in castle[i]:
        cnt_r += 1
 
for j in range(m):
    if "X" not in [castle[i][j] for i in range(n)]:
        cnt_c += 1
 
print(max(cnt_r, cnt_c))