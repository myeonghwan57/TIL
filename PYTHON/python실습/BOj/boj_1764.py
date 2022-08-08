N, M = map(int,input().split())
list1 = []
list2 = []
cnt = 0
for i in range(N):
    list1.append(input())
for j in range(M):
    list2.append(input()) 
who = []
for name in list1:
    for name2 in list2:
        if name == name2:
            who.append(name)
            cnt += 1
print(cnt)
for i in sorted(who):
    print(i)