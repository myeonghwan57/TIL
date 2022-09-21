R, C = map(int,input().split())
p_list = []

for i in range(R):
    p_list.append(input())

result = [0]*5 #인덱스를 부숴야 하는 차의 개수로 활용   

for i in range(R-1):
    for j in range(C-1):
        area = p_list[i][j] + p_list[i][j+1] + p_list[i+1][j] + p_list[i+1][j+1] # 몬스터 트럭이 차지하는 4칸 의 요소를 area에 저장 ex).... , #..# ,XX..
        if '#' in area: # 네칸을 더한 값-> 문자열에 만얀 #(빌딩)이 존재 한다면 continue 
            continue    
        else:           # 빌딩이 존재 하지 않을 경우 
            if area.count('X') == 0:    #부숴야하는 차가 0개일때 네칸 다 '.' 일때
                result[0] += 1         
            elif area.count('X') == 1:  #부숴야하는 차가 1개일때 한칸이 'X' 일때
                result[1] += 1
            elif area.count('X') == 2:
                result[2] += 1
            elif area.count('X') == 3:
                result[3] += 1
            elif area.count('X') == 4:
                result[4] += 1

print(*result, sep='\n')