#백준 1010 다리 놓기

import math
l = int(input())
for i in range(l):
    n, k = map(int, input().split())
    print(math.comb(k, n))