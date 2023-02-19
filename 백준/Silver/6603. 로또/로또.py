#백준 6603 로또
from itertools import combinations
k = 8
while(k!=0):
    lst = list(map(int, input().split()))
    k = lst[0]
    if k == 0:
        break
    del lst[0]
    ans=list(combinations(lst, 6))
    for i in ans:
        i = list(i)
        print(*i, sep = " ")
    print()
        