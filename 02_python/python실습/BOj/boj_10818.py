n = int(input())
numbers = list(map(int,input().split()))
max_num = numbers[0]
min_num = numbers[0]
for i in range(n):
    if max_num < numbers[i]:
        max_num = numbers[i]
    if min_num > numbers[i]:
        min_num = numbers[i]
print(min_num,max_num)
