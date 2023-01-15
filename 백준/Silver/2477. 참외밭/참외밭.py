num = int(input())
lst = [] #전체 순서
lbh = [] #수평길이
lbv = [] #수직길이

for i in range(6):
    a, b = map(int, input().split())
    if a == 1 or a == 2:
        lst.append(b)
        lbh.append(b)
    else:
        lst.append(b)
        lbv.append(b)

bh = max(lbh)
bv = max(lbv)

bhi = lst.index(bh)
bvi = lst.index(bv)

if bhi == 5:
    if lst[0]<lst[bhi-1]:
        sh = lst[0]
    else:
        sh = lst[bhi-1]
else:
    if lst[bhi+1]<lst[bhi-1]:
        sh = lst[bhi+1]
    else:
        sh = lst[bhi-1]

if bvi == 5:
    if lst[0]<lst[bvi-1]:
        sv = lst[0]
    else:
        sv = lst[bvi-1]
else:
    if lst[bvi+1]<lst[bvi-1]:
        sv = lst[bvi+1]
    else:
        sv = lst[bvi-1]


tmp = (bh*sh) + (bv*sv) - (sh*sv)
ans = tmp * num

print(ans)