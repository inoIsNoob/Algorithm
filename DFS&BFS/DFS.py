#DFS는 Depth-First Search 즉 깊이 우선 탐색이다. 노드를 탐색하여 노드와 연결된 가장 깊은 곳(큰 값) 부터 탐색하는 알고리즘이다.
def dfs(graph, v, visited):
    visited[v] = True
    print(v, end=' ')
    
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)
    
graph = [
    [],
    [2,3,8],
    [1,7],
    [1,4,5],
    [3,5],
    [3,4],
    [7],
    [2,6,8],
    [1,7]
    ]

visited = [False] * 9

dfs(graph, 1, visited)
