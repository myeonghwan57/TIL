T = int(input())

for i in range(T):  
    sum = 0
    container = list(map(int,input().split()))
    for j in range(10):
        if container[j]%2 == 1:
            sum = sum+container[j]
    print(f'#{i+1} {sum}')