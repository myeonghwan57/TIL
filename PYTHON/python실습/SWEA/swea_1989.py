T = int(input())

for i in range(T):
    num = 1
    word = list(input())
    for j in range(len(word) // 2):
        if word[j] == word[-1 - j]:
            num = 1
        else:
            num = 0
    print(f'#{i+1} {num}')
