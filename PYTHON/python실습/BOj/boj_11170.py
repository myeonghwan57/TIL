T = int(input())
for _ in range(T):
    n, m = map(int,input().split())
    cnt = 0
    for i in range(n, m+1):
        num_str = str(i)
        for j in num_str:
            if j == '0':
                cnt += 1
    print(cnt)