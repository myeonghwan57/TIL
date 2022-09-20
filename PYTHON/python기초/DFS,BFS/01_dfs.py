def dfs(graph, v, visited):
    # 방문한 곳은 True 로 바꿔준다.
    visited[v] = True 
    # 현재 사용하고 있는 노드 출력
    print(v,end='')
    #연결된 노드에서 방문 안한 곳이 있는지 확인.
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)