def matrix_addition():
    n, m = map(int, input().split())

    a = [list(map(int, input().split())) for _ in range(n)]
    b = [list(map(int, input().split())) for _ in range(n)]

    c = [[a[i][j] + b[i][j] for j in range(m)] for i in range(n)]

    for row in c:
        print(*row)
matrix_addition()