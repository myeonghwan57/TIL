T = int(input())

for i in range(T): 
    numbers =list(map(int,input().split()))
    print(f'#{i+1} {max(numbers)}') 