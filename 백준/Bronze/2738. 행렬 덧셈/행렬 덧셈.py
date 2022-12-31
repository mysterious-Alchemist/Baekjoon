a = []
b = []
m, n = map(int, input().split())

for i in range(m*2):
    tmp = list(map(int, input().split()))
    if(i<m):
        a.append(tmp)
    else:
        b.append(tmp)

for i in range(m):
    for j in range(n):
        sum = (a[i][j]+b[i][j])
        print(sum, end = " ")
    print()