def quickSort(arr):
    if len(arr) <= 1:
        return arr
    
    pivot = arr[0]
    tail = arr[1:]
    
    left = [x for x in tail if x <= pivot]
    right = [x for x in tail if x > pivot]
    
    return quickSort(left) + [pivot] + quickSort(right)

arr = [5,7,9,0,3,1,6,2,4,8]
print(quickSort(arr))
