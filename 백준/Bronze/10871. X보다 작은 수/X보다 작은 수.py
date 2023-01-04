lst = []
lst2 = []
n, x = map(int, input().split())
lst = list(map(int, input().split()))

for i in lst:
  if (x>i):
    lst2.append(i)

for i in lst2:
  print(i, end=" ")