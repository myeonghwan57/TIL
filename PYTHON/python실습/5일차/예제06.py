# N = 10
# answer = ()
# for number in range(N + 1):
#     answer.append(number * 2)

# print(answer)
#'tuple' object has no attribute 'append' -> 튜플은 append 속성을 가지고 있지 않습니다.

#수정 리스트로 수정 
N = 10
answer = []
for number in range(N + 1):
    answer.append(number * 2)

print(answer)