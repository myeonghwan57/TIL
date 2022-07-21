T = int(input())

for i in range(T):
    N = int(input())
    sum = 0
    for j in range(1,N+1):
        if j%2 == 0 :
            sum -= j 
        else:
            sum += j
    print(f'#{i+1} {sum}')