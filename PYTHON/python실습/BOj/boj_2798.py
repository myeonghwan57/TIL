# 블랙잭
N, M = map(int,input().split())
numbers = list(map(int,input().split()))
max_ = 0
for i in range(N-2): #0,1,2,3...n-3 첫번째 고르는 숫자 기준
    for j in range(i+1,N-1):    # 두번재 고르는 숫자
        for k in range(j+1,N):  # 세번째 고르는 숫자 
            total = numbers[i]+numbers[j]+numbers[k]

            if max_ < total <= M:
                max_ = total
            if total == M :
                max_= total
print(max_)
