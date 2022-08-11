import sys
sys.stdin = open("input.txt")

M, N = map(int,input().split())

list_ = [] 

p = [0,0] 

for i in range(N):
    list_.append(list(map(str,input().split())))
    if list_[i][0] == "MOVE":
        x = p[0] + int(list_[i][1])
    elif list_[i][0] == "TURN":
        if list_[i][1] == '0':
            