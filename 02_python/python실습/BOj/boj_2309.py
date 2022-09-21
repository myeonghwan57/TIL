# 일곱 난쟁이
height = []
for i in range(9):  
    height.append(int(input())) # 난쟁이들 키 입력
for i in height:
    for j in height:
        if sum(height) - i - j == 100 and i != j: #7명에 포함 되지 않는 난쟁이 키를 9명의 키를 더한 값에서 빼준값이 100 이라면. 단, 같은 값을 빼는 것은 X
            height.remove(i)                      # 해당 조건을 만족한다면 i, j 인덱스에 해당하는 요소는 필요없는 요소.
            height.remove(j)
height.sort()            
for i in height:
    print(i)