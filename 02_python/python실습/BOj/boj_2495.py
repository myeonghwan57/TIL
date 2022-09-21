for _ in range(3):
    s = str(input())
    max_ = 1
    cnt = 1
    for i in range(1, len(s)):
        if s[i] ==s [i - 1]:
            cnt += 1
        else:
            max_ = max(cnt,max_)
            cnt = 1
    max_ = max(cnt, max_)
    print(max_)