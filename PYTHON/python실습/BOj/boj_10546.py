N = int(input())

name = list(input() for _ in range(N))
success = list(input() for _ in range(N-1))
tmp = {}

for i in range(N):
    if name[i] not in tmp:
        tmp[name[i]] = 1
    else:
        cnt = tmp[name[i]]
        tmp[name[i]] = cnt + 1

for i in range(N-1):
    cnt = tmp[success[i]]
    tmp[success[i]] = cnt -1

for key in tmp:
    if tmp[key] == 1:
        print(key)
        break