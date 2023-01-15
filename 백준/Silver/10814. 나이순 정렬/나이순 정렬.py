import sys
input = sys.stdin.readline

n = int(input())
lst = []

for i in range(n):
    a, b = (map(str, input().split()))
    a = int(a)
    tmp = [a,b,i]
    lst.append(tmp)

lst = sorted(lst, key=lambda x: (x[0], x[2]))

for i in lst:
    print(f"{i[0]} {i[1]}")

    

