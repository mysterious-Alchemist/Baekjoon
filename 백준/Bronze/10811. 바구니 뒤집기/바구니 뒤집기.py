#백준 10813 공 바꾸기
n, m = map(int, input().split())
lst = []
for _ in range(1,n+1):
    lst.append(_)
for _ in range(m):
    i,j = map(int, input().split())
    lst[i-1:j] = lst[i-1:j][::-1]
print(*lst)
