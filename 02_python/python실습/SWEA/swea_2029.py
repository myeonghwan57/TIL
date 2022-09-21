import sys

sys.stdin = open("2029_input.txt", "r")

cnt = int(input())
for i in range(1,cnt+1):
    a,b =map(int,input().split())
    print( "#%d %d %d" % (i, a//b, a%b) )