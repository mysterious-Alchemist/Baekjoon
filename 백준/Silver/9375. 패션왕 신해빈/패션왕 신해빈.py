#백준 9375 패션왕 신해빈 
from itertools import combinations
from functools import reduce
from collections import defaultdict
import sys
input = sys.stdin.readline

x = int(input())
for i in range(x):
    y = int(input())
    if y != 0 :
        dic = defaultdict(lambda:1)
        lst = []
        for i in range(y):
            n, m = map(str, input().split())
            if m not in dic:
                dic[m]
            else:
                dic[m] += 1
        lst = list(dic.values())
        sum = 1
        for i in range(len(lst)):
            sum = sum * (lst[i]+1)
        sum = sum -1
        print(sum)
    else:
        print(0)
