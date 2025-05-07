n,k = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

for _ in range(k):
    a.remove(min(a))
    a.append(max(b))
    b.remove(max(b))

print(sum(a))
##############################################
n,k = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
a.sort()
b.sort(reverse=True)

for i in range(k):
    if a[i] < b[i]:
        a[i], b[i] = b[i], a[i]
    else:
        break

print(sum(a))
