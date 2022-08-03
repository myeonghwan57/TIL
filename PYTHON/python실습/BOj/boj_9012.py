# 괄호
N=int(input())

for _ in range(N):
    cnt = 0
    list_ = list(input())
    for i in range(len(list_)):
        if list_[i] == "(":
            cnt += 1
        else:
            cnt -= 1
        if cnt < 0:
            break
    if cnt == 0:
        print("YES")
    else:
        print("NO")

N=int(input())
left =[]
right = []
for i in range(N):
    list = list(input())
    for j in list:
        if j == '(':
            left.append(j)
        if j == ')':
            right.append(j)
            if len(left) != 0:
                left.pop()
            else:
                right.append(j)
if len(left) == 0 and len(right) == 0:
    print("YES")
else :
    print('NO')
