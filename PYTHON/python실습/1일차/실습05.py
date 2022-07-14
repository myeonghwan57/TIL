num_list = list(map(int, input().split()))
sum = 0
count = 0
for i in num_list:
    sum += i
    count +=1   
print(sum/count)  
