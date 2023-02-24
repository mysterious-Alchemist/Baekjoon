#백준 10813 공 바꾸기
n, m = map(int, input().split())
dic = {}
for _ in range(1,n+1):
    dic[_] = _
for _ in range(m):
    i,j = map(int, input().split())
    tmp1 = dic[j]
    tmp2 = dic[i]
    dic[j] = tmp2
    dic[i] = tmp1
print(*dic.values())