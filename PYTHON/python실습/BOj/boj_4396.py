n = int(input())
bomb = []
game = []
for _ in range(n):
    bomb.append(list(input()))
for _ in range(n):
    game.append(list(input()))
result = [[0 for _ in range(n)] for _ in range(n)]

for i in range(n):
    for j in range(n):
        if bomb[i][j] == '*':
            if game[i][j] =
                