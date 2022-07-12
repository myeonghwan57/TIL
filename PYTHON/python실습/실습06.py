num_list = list(map(int, input().split()))
max = num_list[0]
for i in num_list:
    if i > max :
        max = i
   
print(max)