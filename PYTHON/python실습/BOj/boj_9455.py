T = int(input())
for i in range(T):

    m, n = map(int,input().split())
    square = []
    for i in range(m):
        square.append(list(map(int,input().split())))
    cnt = 0
    for j in range(n): #각 열에 해당하는 행의 값을 사용하기 위해 범위를 n으로 먼저 지정
        base = m - 1  # 바닥의 높이.
        for i in range(m-1,-1,-1): 
            if square[i][j] == 1:
                cnt += base - i  #이동거리 base를 기준으로 상자가 있는 위치의 행의 높이 만큼 아래로 내려가야 하기때문.
                base -= 1 #바닥의 높이 1증가 (-1인 이유는 i,즉 행을 역순으로 for문을 반복했기 때문에 아래서부터 올라오는 개념.)
    print(cnt)        
