#카드 1

N = int(input())
card_list = []
card_stack = []
for i in range(N):
    card_list.append(i+1)

for j in range(N):
    card_stack.append(card_list.pop(0))
    if len(card_list) == 0: # 빈 리스트에서는 pop() 사용할수 없음 -> 빈리스트 일 경우 break 
        break
    card_list.append(card_list.pop(0))
print(*card_stack)
