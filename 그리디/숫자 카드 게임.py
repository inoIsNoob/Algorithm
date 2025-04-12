n,m=map(int,input().split())
res=1

for i in range(n):
  data = list(map(int,input().split()))
  minValue = min(data)
  res = max(minValue, res)

print(res)
