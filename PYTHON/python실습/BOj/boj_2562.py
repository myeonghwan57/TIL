num = []
for i in range(9):
    num.append(int(input()))
    max = num[0]
    idx = 0
    for j in range(len(num)):
        if max < num[j]:
            max = num[j]
            idx = j
print(max, idx+1, sep ='\n')