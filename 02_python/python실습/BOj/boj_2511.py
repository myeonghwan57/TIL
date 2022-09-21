# AB 에게 각각 카드 10 장 
# 승점이 같으면 가장 마지막 승부 
# 아예 비기는 경우는 전부다 D 일때
# W : 3 D : 1 L : 0
A_list = list(map(int,input().split()))
B_list = list(map(int,input().split()))
score = []
for i in range(10):
    if A_list[i] > B_list[i]:
        score.append('A')
    elif A_list[i] < B_list[i]:
        score.append('B')
    else:
        score.append('D')

A_score = score.count('A')*3 + score.count('D')
B_score = score.count('B')*3 + score.count('D')

print(A_score,B_score)
if A_score > B_score:
    print('A')
elif B_score > A_score:
    print('B') 
elif B_score == A_score and A_score == 10:
    print('D')
else : 
    for j in range(-1,-9,-1):
        score[j] != 'D'
        print(score[j])
        break
