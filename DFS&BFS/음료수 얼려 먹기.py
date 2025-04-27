def dfs(x, y):
  if x<0 or y<0 or x>=n or y>=m:
    return False
 
  if graph[x][y] == '0':
    graph[x][y] = '1'
    dfs(x+1, y)
    dfs(x-1, y)
    dfs(x, y+1)
    dfs(x, y-1)
    return True
  return False

n,m = map(int, input().split())
graph = []
cnt = 0

for _ in range(n):
  graph.append(list(input()))

for i in range(n):
  for j in range(m):
    if dfs(i, j):
      cnt += 1

print(cnt)
