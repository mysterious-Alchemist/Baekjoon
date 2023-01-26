# 동전 0
n, m = map(int, input().split())

lst = [int(input()) for i in range(n)]
lst.sort(reverse=True)
c = 0
for i in range(len(lst)):
    if m >= lst[i]:
        c = m // lst[i] + c
        m = m % lst[i]
    if m == 0:
        break
print(c)