import sys

a = sys.stdin.readline()
t = int(a)
lst = []

for i in range(t):
    a, b = map(int, sys.stdin.readline().split())
    print(a+b)