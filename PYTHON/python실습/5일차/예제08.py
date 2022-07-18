# word = "HappyHacking"
# 
# count = 0
# for char == "a" or "e" or "i" or "o" or "u":
#     if char in vowels:
#         count += 1

# print(count)

#or의 잘못된 사용으로 결과 값이 달라짐

# 수정 for문에서 or 를 사용하지 않고 모음 리스트를 만들어 비교하도록 수정.
word = "HappyHacking"
vowels=['a','e','i','o','u']
count = 0
for char in word:
    if char in vowels:
        count += 1

print(count)
