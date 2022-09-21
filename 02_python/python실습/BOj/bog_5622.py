# 다이얼
dial = {
    0 : '', 1 : '',
    2 : 'ABC', 3 : 'DEF', 4 : 'GHI', 5 : 'JKL',
    6 : 'MNO', 7 : 'PQRS', 8 : 'TUV', 9 : 'WXYZ',
}
word = input()
upper_word = word.upper()
cnt = 0
for i in upper_word:
    for j in dial:
        if i in dial[j]:
            cnt  += j+1
print(cnt)

