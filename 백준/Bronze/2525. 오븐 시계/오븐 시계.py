h, m = map(int, input().split())
r = int(input())

m1 = m + r
d = m1 // 60 
e = m1 % 60

if d > 0:
    h = h + d
    if h>23:
      h = h % 24

print(h,e)