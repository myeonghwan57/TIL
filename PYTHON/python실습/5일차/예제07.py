# number_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# total = 0
# count = 0

# for number in number_list:
#     total += number
# count += 1

# print(total // count)

# count 의 들여쓰기 위치와 나누기 연산자 오류

#수정 count를 for 문 안에서 동작을 할수 있도록 들여쓰기, 나누기 연산자를 '/' 로 수정.

number_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

total = 0
count = 0

for number in number_list:
    total += number
    count += 1

print(total / count)