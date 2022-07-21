T = int(input())

for i in range(T):
    N = list(map(int, input().split()))
    h = N[0] + N[2]
    m = N[1] + N[3]
    if h > 12:
        h = h - 12
    if m > 60:
        h += 1
        m = m - 60
    print(f'#{i+1} {h} {m}')    