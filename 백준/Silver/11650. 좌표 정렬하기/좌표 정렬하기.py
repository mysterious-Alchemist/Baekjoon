import sys
input = sys.stdin.readline

n = int(input())
lst = []
for i in range(n):
    lst.append(list(map(int, input().split())))

lst = sorted(lst, key=lambda x: (x[0], x[1]))

for i in lst:
    print(f"{i[0]} {i[1]}")