arr = [1,5,9,0,3,1,6,2,9,1,4,8,0,5,2]
maxValue,minValue = arr[0],arr[0]
for i in arr:
    if i > maxValue: maxValue = i
    
box = [0] * (maxValue+1)

for i in arr:
    box[i] += 1

for i in range(len(box)):
    for j in range(box[i]):
        print(i, end=' ')
