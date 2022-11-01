# 어떤 지원자 성적이 다른 모든 지원자 성적에 비해 적어도 하나가 안떨어지면 뽑음
# 어떤 지원자 A가 다른 지원자의 성적보다 하나라도 높은게 없으면 탈락.
import sys

input = sys.stdin.readline
T = int(input())
for _ in range(T):
    N = int(input())
    score = []
    for _ in range(N):
        rank1, rank2 = map(int, input().split())
        score.append([rank1, rank2])

    score = sorted(score, key=lambda x: x[0])
    min = score[0][1]
    cnt = 1
    for i in range(N):
        if min > score[i][1]:
            min = score[i][1]
            cnt += 1
    print(cnt)
