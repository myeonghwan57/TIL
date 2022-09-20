# 너비 우선 탐색 큐 자료구조를 이용 
# 탐색 시작 노드에 큐에 삽입 방문 처리
# 인접한 노드를 한번에 큐에 삽입. 특정 조건의 최단경로 
from collections import deque
import queue

def bfs(graph, start, visited):
    queue = deque([start])

    visited[start] = True
    while queue:
        v = queue.popleft() 
        print(v,end='')

        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True