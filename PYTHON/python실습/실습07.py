num_list = list(map(int, input().split()))
min = num_list[0]
for i in num_list:
    if i < min :
        min = i
   
print(min)