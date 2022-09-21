N=int(input())
dic={}
cnt=0
for _ in range(N):
    name = input()

    if name == "ENTER":
        for key,value in dic.items():
            if value==1:
                cnt+=1
        dic={}
    else:
        if name not in dic:
            dic[name] = 1

for key,value in dic.items():
    if value == 1:
        cnt += 1
print(cnt)