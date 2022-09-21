#직사각형 넓이 구하기. (해설 참고)
xy_list = [[0 for _ in range(101)] for _ in range(101)]  # 모든 요소가 '0'으로 초기화된 101x101행렬 선언.
for _ in range(4):
    x1, y1, x2, y2 = map(int, input().split()) #사각형은 나타내는 좌표 입력.
    
   
    for i in range(x1, x2):
        for j in range(y1, y2):
            xy_list[i][j] = 1  #각 좌표에 해당하는 사각형의 부분만 1로 바꿔준다.

result = 0

for row in xy_list: 
    result += sum(row) # 101x101 행렬의 모든 요소 합-> 입력받은 좌표의 사각형을 1로 바꿔준 부분의 합 

print(result)