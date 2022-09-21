#절대값의 힙 
import heapq
import sys
N = int(input())
heap = []
for _ in range(N):
    x = int(sys.stdin.readline())
    if x != 0: 
        heapq.heappush(heap,(abs(x),x))# 튜플을 사용할 경우 첫번째 항목을 기준으로 우선순위 생성. 첫번째 항목은 절대값   
    else:
        if heap: 
            print(heapq.heappop(heap[1])) # 절대값 항목으로 나열된 heap 에서 최저값을 pop을 사용하여 print 
        else:     
            print(0)

