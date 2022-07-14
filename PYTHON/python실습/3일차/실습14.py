#문자열 word가 주어질 때, 해당 문자열에서 a 개수를 구하세요.
#count() 메서드 사용 금지
word = input()
count=0 #a 의 개수를 세기 위한 변수 0 으로 초기화
for i in word:
    if i == 'a':
        count+=1
print(count)