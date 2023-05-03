#2675 문자열 반복
n = int(input())
for i in range(n):
    a, b = map(str, input().split())
    a = int(a)
    lst = list(map(str, b))

    for i in lst:
        print(i*a, end = "")
    print()