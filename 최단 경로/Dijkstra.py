def getSmallestNode():
  minValue = INF
  index = 0
  for i in range(1, n + 1):
    if distance[i] < minValue and not visited[i]:
      minValue = distance[i]
      index = i
  
  return index

def dijkstra(start):
  distance[start] = 0
  visited[start] = True
  for j in graph[start]:
    distance[j[0]] = j[1]
  
  for i in range(n - 1):
    now = getSmallestNode()
    visited[now] = True
    for j in graph[now]:
      cost = distance[now] + j[1]
      if cost < distance[j[0]]:
        distance[j[0]] = cost

INF = int(1e9)
n, m = map(int, input().split())
start = int(input())
graph = [[] for i in range(n + 1)]
visited = [False] * (n + 1)
distance = [INF] * (n + 1)

for _ in range(m):
  a, b, c = map(int, input().split())
  graph[a].append((b,c))

dijkstra(start)

for i in range(1, n + 1):
  if distance[i] == INF:
    print('Infinity')
  else:
    print(distance[i])
