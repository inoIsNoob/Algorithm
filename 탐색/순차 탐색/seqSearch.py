def sequencialSearch(n, target, arr):
    for i in range(n):
        if arr[i] == target:
            return str(i)

arr = ['최','인','호','입','니','다']
target = '입'
n = len(arr)

print(sequencialSearch(n, target, arr) + '번째 index')
