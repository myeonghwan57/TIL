#나머지
num_dict = {}
# 입력 받은 수 map
num = map(int,input().split())
# 주어진 수를 사용하여 나머지를 키값으로 하는 딕셔너리 생성 나머지 값이 같다면 
# 즉, 키 값이 같다면 +1 존재하지 않았던 값이라면 키 생성후 1로 초기화 
for i in num:  
    if i % 42 not in num_dict:
        num_dict[i % 42] = 1
    else:
        num_dict[i % 42] += 1
print(len(num_dict))
