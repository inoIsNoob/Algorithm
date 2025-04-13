c = input()
x = ord(c[0])-96
y = int(c[1])
cnt=0

possibleMove=[(x-2, y+1), (x-1, y+2),
              (x+1, y+2), (x+2, y+1),
              (x+1, y-2), (x+2, y-1),
              (x-2, y-1), (x-1, y-2)]


for i in possibleMove:
    if i[0]*i[1] > 0:
        cnt += 1

print(cnt)
