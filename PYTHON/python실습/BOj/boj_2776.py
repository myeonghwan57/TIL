import sys 
input = sys.stdin.readline
T = int(input())
for _ in range(T):
    N = int(input())
    num_1 = list(map(int,input().split())) 
    M = int(input())
    num_2 = list(map(int,input().split())) 
    for i in num_2:
        if i in num_1:
            print('1')
        else:
            print('0') 


