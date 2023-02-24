#백준 10810 공 넣기
n, m = map(int, input().split())
dic = {}
for _ in range(1,n+1):
    dic[_] = 0
for _ in range(m):
    i,j,k = map(int, input().split())
    for c in range(i,j+1):
        dic[c] = k
print(*dic.values())