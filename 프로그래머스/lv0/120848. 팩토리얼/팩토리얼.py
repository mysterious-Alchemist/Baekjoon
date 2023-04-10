import sys
sys.setrecursionlimit(10**6)
memo = {}
def tmp(n):
    if n in memo:
        return memo[n]
    if n != 1:
        tmp_sum = n * tmp(n-1)    
        memo[n] = tmp_sum
        return tmp_sum
    elif n == 1:
        memo[1] = 1
        return 1
    
def solution(n):
    answer = 1
    while(tmp(answer)<n):
        answer = answer + 1
    if tmp(answer)>n:
        answer  = answer -1
    return answer
