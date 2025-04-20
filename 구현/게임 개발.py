n,m = map(int, input().split())
a,b,d = map(int, input().split())
dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]
maap = []
cnt,beenCnt = 0,1
for _ in range(n):
    maap.append(input().split())

maap[a][b] = '2'
while True:
    d = 3 if d-1==-1 else d-1
    if maap[a+dy[d]][b+dx[d]] == '0':
        maap[a+dy[d]][b+dx[d]] = '2'
        a += dy[d]
        b += dx[d]
        beenCnt += 1
        cnt = 0
    else:
        cnt += 1
    
    if cnt >= 4: #네 면 x
        a -= dy[d]
        b -= dx[d]
        if maap[a][b] == '1':
            break
    
print(beenCnt)
