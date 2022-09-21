# 킹의 위치, 돌의 위치, 움직이는 횟수
p1, p2, N = map(str,input().split())
# 킹의 위치, 돌의 위치 좌표로 변환
pk = [ord(p1[0])-64,int(p1[1])]
ps = [ord(p2[0])-64,int(p2[1])]
# 움직일수 있는 8방향 딕셔너리 생성
move = {
        'R': [1, 0],
        'L': [-1, 0], 
        'B': [0, -1], 
        'T': [0, 1], 
        'RT': [1, 1], 
        'LT': [-1, 1], 
        'RB': [1, -1], 
        'LB': [-1, -1]
}
# 움직임 N 횟수 만큼 입력 받음.
for _ in range(int(N)):
    M  = input()
# 입력한 움직임을 키로 활용하여 그 해당 움직임에 대한 이동(value)을 현재의 위치점에다가 더해줌
    pk[0] += move[M][0]
    pk[1] += move[M][1]
    # 킹의 위치가 체스판 안에 있다면 
    if 0 < pk[0] < 9 and 0 < pk[1] < 9:
    # 그 위치가 돌의 위치와 같다면 킹이 움직인 같은 방향으로 돌을 이동시킴
        if pk == ps:
            ps[0] += move[M][0]
            ps[1] += move[M][1]
            # 돌의 위치가 벗어난다면 돌, 킹 둘다 움직이지 않는다.
            if 0 < ps[0] < 9 and 0 < ps[1] < 9:
                continue
            else:
                pk[0] -= move[M][0]
                pk[1] -= move[M][1]
                ps[0] -= move[M][0]
                ps[1] -= move[M][1]
    #킹의 위치가 체스판을 벗어나면 이동하지 않음.
    else: 
        pk[0] -= move[M][0]
        pk[1] -= move[M][1]

print(chr(pk[0]+64)+str(pk[1]))
print(chr(ps[0]+64)+str(ps[1]))


