#하얀칸
N = []
cnt = 0
for _ in range(8):
    N.append(list(map(str, list(input()))))


for i in range(8):
    for j in range(8):
        if (i + j) % 2 == 0: #하얀칸일 경우
            if N[i][j] == 'F': #F있을 경우
                cnt += 1
print(cnt)