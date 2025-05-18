n,m = map(int, input().split())
coin = list()
for _ in range(n):
  coin.append(int(input()))

d = [10001] * (m+1)
d[0] = 0 
for i in coin:
  for j in range(i, m+1):
    if d[j-i] != 10001:
      d[j] = min(d[j], d[j-i] + 1)

print(d[m] if d[m]!=10001 else -1)
