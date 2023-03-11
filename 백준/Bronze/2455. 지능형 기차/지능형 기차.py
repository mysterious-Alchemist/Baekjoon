t = 0
h = 0
for i in range(4):
    m, p = map(int, input().split())
    t = t - m + p
    if t>h:
        h = t
print(h)