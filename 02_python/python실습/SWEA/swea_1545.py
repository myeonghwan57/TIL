import sys

sys.stdin = open("swea_input_1545.txt", "r")

n = int(input())

for i in range(n+1):
    print(n-i,end=' ')