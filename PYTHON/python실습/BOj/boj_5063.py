import sys 

N = int(input())
for i in range(N):
    r, e, c = map(int,sys.stdin.readline().split())
    # r = 광고 x 수익 e = 광고 o 수익 c = 광고 비용
    #광고 했을때 
    if r < e - c:
        print('advertise')
    elif r + c > e:
        print('do not advertise')
    else:
        print('does not matter') 


    