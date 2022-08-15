T = int(input())

for i in range(T):  
    string = input()
    word = ''
    for char in string:
        word += char
        length = len(word)
        if word == string[length:length+length]:
            break
    print(f'#{i+1} {len(word)}')