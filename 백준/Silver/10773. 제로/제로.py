from collections import deque
import sys

input = sys.stdin.readline

k = int(input())

deq = deque()

for i in range(k):
    num = int(input())
    if num == 0:
        deq.pop()
    else:
        deq.append(num)

print(sum(deq))