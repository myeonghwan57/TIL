# words = list(map(int, input().split()))
# print(words)

# invalid literal for int() with base 10: "I'm" -> int에 허용되지 않은 값인 "I'm" 이 들어갔다.

#수정 str 타입으로 변환
words = list(map(str, input().split())) 
print(words)