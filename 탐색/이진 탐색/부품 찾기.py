def search(parts, finds, number, n):
    start, end = 0, n-1
    while start <= end:
        mid = (start + end) // 2
        
        if parts[mid] < number:
            start = mid + 1
        elif parts[mid] > number:
            end = mid - 1
        else:
            return True
    
    return False
    
n = int(input())
parts = sorted(list(map(int, input().split())))
m = int(input())
finds = list(map(int, input().split()))

for i in finds:
    if search(parts, finds, i, n): print('yes',end=' ')
    else: print('no',end=' ')
