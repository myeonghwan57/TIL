K = int(input())

for i in range(K):
    max_gap = 0
    score_list = list(map(int,input().split()))
    del score_list[0]
    score_list.sort(reverse= True)
    for j in range(len(score_list)-1):
        gap = score_list[j] - score_list[j+1] 
        if max_gap < gap:
            max_gap = gap
    print(f'Class {i+1}')
    print(f'Max {max(score_list)}, Min {min(score_list)}, Largest gap {max_gap}')