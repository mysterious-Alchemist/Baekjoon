#백준 9711 피보나치
import sys
sys.setrecursionlimit(10**7)

dic = { 1:1, 2:1 }

def fib(n):
    if n in dic:
        return dic[n]
    else:
        ans = fib(n-1) + fib(n-2)
        dic[n] = ans
        return ans
n = int(input())
for i in range(n):
    p, q = map(int, input().split())
    print(f"Case #{i+1}: {fib(p)%q}")