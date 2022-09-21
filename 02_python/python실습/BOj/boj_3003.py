# 킹 1개, 퀸 1개, 룩 2개, 비숍 2개, 나이트 2개, 폰 8개
C = [1, 1, 2, 2, 2, 8]
li = list(map(int,input().split()))
result = []
for i in range(len(C)):
    cnt = 0
    while True:
        if li[i] == C[i]:
            break
        if li[i] > C[i]:
            li[i] -= 1
            cnt -= 1
            if li[i] == C[i]:
                break
        elif li[i] < C[i]:
            li[i] += 1
            cnt += 1
            if li[i] == C[i]:
                break
    result.append(cnt)
print(*result)   
