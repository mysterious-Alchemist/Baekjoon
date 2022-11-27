from collections import Counter

a = input()
C = Counter(a.upper())

lst1 = list(C.values())
m = lst1.count(max(lst1))
#lst = list(dic.value())

if (m == 1):
  print(max(C, key=C.get).upper())
else:
  print("?")