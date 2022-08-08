N = int(input())
card_dic = {}
for i in range(N):
    num = int(input())
    if num not in card_dic:
        card_dic[num] = 1
    else: 
        card_dic[num] += 1

result = sorted(card_dic.items(),key = lambda x : (-x[1],x[0])) # 두번째 인자로 내림차순 , 첫번째 인자로 오름차순
print(result[0][0])