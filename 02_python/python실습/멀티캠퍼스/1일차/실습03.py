#1) while 문
n = int(input())
count = 0
sum = 0 
while count <= n:
    sum += count
    count+=1
print(sum)

#2) for 문
total = 0
for i in range(0,n+1):
    total += i
print(total)
