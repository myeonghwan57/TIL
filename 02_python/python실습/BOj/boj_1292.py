#쉽게 푸는 문제
#1 2 2 3 3 3 4 4 4 4 5 .. => 3 ~ 7
# 문제의 수 = n(n+1)/2  ex) b = 7  n = 4일 경우에 총 문제의 개수는 10문제 7은 10문제 사이에 존재 

a, b = map(int,input().split())
# 리스트 선언 처음 인덱스에 0 대입 -> 주어진 문제가 1 22 333 4444 로 이어지기때문에.
data=[0]
# 구간의 합 저장할 변수 선언 초기화
sum=0

for i in range(1,b+1): # i는 1 부터 b+1까지 
  for j in range(i): #J는 0부터 i까지 
    data.append(i) # ex) i 1일때 j = 0 data = [0] 뒤에 1 대입 -> i = 2 일때 j = 0, 1 data = [0,1]에 j=0일때 한번 j= 1일때 한번 씩 2 대입  
print(data)
for i in range(a, b+1):
  sum+=data[i]
print(sum)