# 한개의 회의실 N개의 회의 -> 시간표 작성
# 각 회의 I 에 대해 시작 시간 끝나는 시간 겹치지 않게 회의실 사용할 수 있는 회의의 최대 갯수
# 회의는 중간에 중단 X 한 회의가 끝남과 동시에 다음 회의 진행 O

# 11
# 1 4
# 3 5
# 0 6
# 5 7
# 3 8
# 5 9
# 6 10
# 8 11
# 8 12
# 2 13
# 12 14

N = int(input())
time_list = []
for _ in range(N):
    start, end = map(int, input().split())
    time_list.append([start, end])
# 회의 갯수
cnt = 0
# 시작시간 오름 차순
time_list = sorted(time_list, key=lambda x: x[0])
# 끝나는 시간 오름차순
time_list = sorted(time_list, key=lambda x: x[1])
end_time = 0
for i, j in time_list:
    if end_time <= i:
        cnt += 1
        end_time = j
print(cnt)
