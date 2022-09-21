vowels = ['A','E','I','O','U']
while True:
    str = input().upper()
    if str == '#':
        break
    cnt = 0
    for i in str:
        if i in vowels:
            cnt += 1
    print(cnt)