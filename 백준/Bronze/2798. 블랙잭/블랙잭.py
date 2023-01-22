from itertools import combinations

n, m = map(int, input().split())
lst = list(map(int, input().split()))
lst2 = []
for i in combinations(lst, 3):
  if m>=sum(i):
    lst2.append(sum(i))
print(max(lst2))
