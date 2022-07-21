t=int(input())

for i in range(t):
    print('#%s' %(i+1),end=' ')
    date=input()
    year=int(date[:4])
    month=int(date[4:6])
    dd=int(date[6:])
    if month <1 or month>12:
        print(-1)
        continue

    if month in [1,3,5,7,8,10,12]:
        if dd <1 or dd>31:
            print(-1)
            continue
    if month ==2:
        if dd<1 or dd>28:
            print(-1)
            continue

    if month in [4,6,9,11]:
        if dd <1 or dd>30:
            print(-1)
            continue
    print("%04d/%02d/%02d" %(year,month,dd))
