#데이터가 정렬되어 있을때만 사용 가능함.
def binarySearch(arr, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        
        if arr[mid] > target:
            end = mid - 1
        elif arr[mid] < target:
            start = mid + 1
        else:
            return mid
    
    return 0

arr = [1,3,5,6,8,9,11,13,15,17,19,21,25,30]
target = 21
print(binarySearch(arr, target, 0, len(arr)-1) ,'번째 index')
