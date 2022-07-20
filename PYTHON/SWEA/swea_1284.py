T = int(input())

for i in range(T):
    A=0
    B=0
    P,Q,R,S,W =map(int,input().split())
    A = W*P
    B=Q
    if R < W:
        B += S*(W-R)
        
    if A>B:
        print(f'#{i+1} {B}')
    else:
        print(f'#{i+1} {A}')

#p -> A사 리터당 p원 
#Q -> B사 R 리터 이하인경우 리터당 Q원 // 넘으면 S요금 
# W-> 사용한 리터 