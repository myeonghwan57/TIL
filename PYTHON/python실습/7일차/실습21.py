n = int(input())
num_list = []

while n:
    num_list.append(n%10)
    n=n//10
for i in range(len(num_list)):
    print(num_list[i], end='')