#1) while 문
n = int(input())
count = 0
mul = 1 
while count < n:
    mul *= (count+1)
    count+=1
print(mul)

#2) for 문
total = 1
for i in range(1,n+1):
    total *= i
print(total)
