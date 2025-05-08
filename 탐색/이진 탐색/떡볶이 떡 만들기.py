n,m = map(int, input().split())
height = list(map(int, input().split()))
start, end = 0, max(height)

while start <= end:
    mid = (start + end) // 2
    getRice = 0
    for i in height:
        if i > mid:
            getRice += i - mid
    
    if getRice < m:
        end = mid - 1
    elif getRice > m:
        start = mid + 1
    else:
        break

print(mid)
