# 수정렬하기 오름 차순으로 정렬
N = int(input())
num_list = []
for i in range(N):
    num_list.append(int(input()))
sorted_list = sorted(num_list)
for i in range(len(num_list)):
    print(sorted_list[i])