N = int(input())

stack = [] # 정수를 저장하는 스택.
words = []
for i in range(N):
    words.append(input())
for word in words:
    if word == 'push':
        
        