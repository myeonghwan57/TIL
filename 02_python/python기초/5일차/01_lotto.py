import random #의사 난수 생성. 

n= int(input())
for i in range(n):
    numbers=random.sample(range(1,46),6)
    numbers.sort()
    print(numbers,type(numbers))# 알아서 리스트로 만들어 준다