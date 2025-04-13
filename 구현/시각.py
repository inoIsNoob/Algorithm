n=int(input())
h,m,s,res=0,0,0,0

while True:
    s += 1
    if s == 60:
        m += 1
        s = 0
    if m == 60:
        h += 1
        m = 0
    if '3' in str(h)+str(m)+str(s):
        res += 1
    if (h == n) and (m == 59) and (s == 59): break

print(res)
