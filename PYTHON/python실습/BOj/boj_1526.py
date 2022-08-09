n=int(input())
while True:
    cnt=0
    for i in str(n):
        if i!="4" and i!="7":
            cnt=1
            n-=1
    if cnt==0:
        print(n)
        break