#숫자 카드 2 -> 다시 보기
N = int(input())
card_list = list(map(int,input().split()))
M = int(input())
num_list = list(map(int,input().split()))

cnt = {}
# 카드의 숫자에 대해서 딕셔너리 생성 후 중복되는 수 카운트 
for i in card_list:
    if i in cnt:
        cnt[i] += 1
    else:
        cnt[i] = 1
# 주어진 숫자가 카드 딕셔너리에 존재 한다면 해당 숫자의 value 즉, 카운트 수를 출력 없는 숫자면 0 을 출력.
for i in num_list:
    if i in cnt:
        print(cnt[i], end=' ')
    else: 
        print(0, end=' ')