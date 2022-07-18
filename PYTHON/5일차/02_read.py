# 파일명을 어떤 모드로 열지 설정 rwx
with open('test.txt', 'r',encoding='utf-8') as f:
    text = f.read()
    print(text) # str
    names = text.split()
    count = 0
    for name in names:
        if name[1] == '번': #if name.startswith('김'):
            count+=1
    print(count) 
