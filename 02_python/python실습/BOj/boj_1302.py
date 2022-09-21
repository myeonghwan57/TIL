N = int(input())
dic = {}
for i in range(N):
    book = input()
    if book not in dic:
        dic[book] = 1
    else: 
        dic[book] += 1
print(sorted(list(dic.items()), key = lambda x : (-x[1],x[0]))[0][0])