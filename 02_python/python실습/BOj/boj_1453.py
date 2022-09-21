N = int(input())
numbers = list(map(int,input().split()))
cnt = 0
pc_list = [0]*101
for i in numbers:
    if pc_list[i] == 0 :
        pc_list[i] += 1
    else:
        cnt += 1
    
print(cnt)
