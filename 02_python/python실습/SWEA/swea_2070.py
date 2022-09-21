import sys

sys.stdin = open("swea_input_2070.txt", "r")

T = int(input())
for i in range(T):
    a,b =map(int,input().split())
    if a>b:
        print(f'#{i+1} >')
    elif a == b:
        print(f'#{i+1} =')
    else:
        print(f'#{i+1} <')