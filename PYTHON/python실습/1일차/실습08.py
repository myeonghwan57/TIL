num_list = list(map(int, input().split()))
tmp = 0
for i in range(len(num_list)):
    for j in range(i+1,len(num_list)):
        if num_list[i] > num_list[j]:
            tmp = num_list[i]
            num_list[i]=num_list[j]
            num_list[j] = tmp

print(num_list[len(num_list)-2])

