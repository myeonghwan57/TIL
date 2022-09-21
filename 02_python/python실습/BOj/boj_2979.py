A, B, C = map(int,input().split())

arr = [0] * 100 
sum_ = 0
for _ in range(3):
    start, end = map(int, input().split())
    for i in range(start, end):
        arr[i] += 1
for j in arr:
    sum_ += {0:0, 1:A, 2:B*2, 3:C*3}[j]
print(sum_)