N = int(input())
room = []
for _ in range(N):
    room.append(list(input()))  # 방 리스트에 '.',' X' 입력 

cnt_list =[0,0] # 카운트 리스트 각각 행 과 열에 대한 누울수 있는 공간 있으면 카운트.

for i in range(N):
    cnt_r = 0 #행에 대한 공간 카운트 
    for j in range(N):
        if room[i][j] == '.': # i,j의 공간이 '.'이라면 (cnt_r)카운트에 +1을 해준다.
            cnt_r += 1
        else:           # 'X' 라면 cnt_r 0으로 초기화
            cnt_r = 0
        if cnt_r == 2: # 어느 공간에 상관없이 cnt_r이 2가 되면 연속으로 이루어진 두칸의 공간 의미-> 카운트 리스트에 1을 더해줌.
            cnt_list[0] += 1

for j in range(N):
    cnt_c = 0
    for i in range(N):
        if room[i][j] == '.':
            cnt_c += 1
        else: 
            cnt_c = 0
        if cnt_c == 2:
            cnt_list[1] += 1

print(cnt_list[0], cnt_list[1])







# cnt_list =[0,0]

# for i in range(N):
#     cnt_r = 0
#     for j in range(N-1):
#         if room[i][j] == room[i][j+1] == '.':
#             cnt_r += 1
#     if cnt_r >= 1:
#         cnt_list[0] += 1

# for j in range(N):
#     cnt_c = 0
#     for i in range(N-1):
#         if room[i][j] == room[i+1][j] == '.':
#             cnt_c += 1
#     if cnt_c >= 1:
#         cnt_list[1] += 1

# print(cnt_list[0], cnt_list[1])
