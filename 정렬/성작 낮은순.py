N = int(input())
grade = dict()

for _ in range(N):
    name, score = input().split()
    grade[int(score)] = name

for i in sorted(grade):
    print(grade[i], end=' ')
