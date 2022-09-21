import sys

sys.stdin = open("swea_input_2071.txt", "r")

T = int(input())
for i in range(T):
    numbers = list(map(int,input().split()))
    sum = 0
    for j in range(10):
        sum += numbers[j]
    
    print('#%d %d' %(i+1, round(sum/10)))
        