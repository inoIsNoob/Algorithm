# 25.04.12 / 1이 될 때까지
n,k = map(int, input().split())
res = 0

while True:
  divvy=n//k*k
  res += n-divvy
  n = divvy
  
  if n<k:
    break
    
  res += 1
  n = n//k

print(res+n-1)
