#N의 배수 번호인 양을 세기로 함 
#첫번째는 N번 양을 세고 두번째는 2N번 셈 
T = int(input())
for i in range(T): #케이스 수 
    N = int(input()) #
    numbers = []
    cnt = 1 
    while len(numbers) < 10:
        CN = cnt*N
        for j in str(CN):
            if j not in numbers:
                numbers.append(j)      
        cnt+=1
    print(f'#{i+1} {CN}')
















    

