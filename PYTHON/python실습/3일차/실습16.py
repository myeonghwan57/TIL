# 문자열 word가 주어질 때, 해당 문자열에서 모음의 갯수를 출력하시오.
# 모음 : a, e, i, o, u 
# count() 사용 금지

word = input()
vowels = ['a','e','i','o','u']
count = 0
for i in vowels:
    for j in word:
        if i == j:
            count+=1
print(count)