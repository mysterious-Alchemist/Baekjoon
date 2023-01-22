from itertools import combinations

n, m = map(int, input().split())
lst = list(map(int, input().split()))

lstc = list(combinations(lst, 3))
for i in range(len(lstc)):
  lstc[i] = sum(lstc[i])

def under_m(lst):
  return m>=lst
lsta = list(filter(under_m, lstc))
print(max(lsta))