n = int(input())
new_n = n
cnt = 0
while True:
    a = n//10
    b = n % 10
    c = (a + b) % 10
    new_n = (b * 10) + c

    cnt += 1
    if (new_n == n):
        break
print(cnt)