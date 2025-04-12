# 25.04.10 / 큰 수의 법칙
n,m,k=map(int,input().split())
data=sorted(list(map(int,input().split())))
cnt,res = 0,0

for i in range(m):
    cnt += 1
    maxValue = data[-1]
    if cnt > k:
        cnt = 0
        maxValue = data[-2]

    res += maxValue

print(res)
