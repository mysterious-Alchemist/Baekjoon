from collections import deque 
n, k = map(int, input().split())
q = deque([i for i in range(1, n+1)])
ans = deque()
while q:
    q.rotate(-k+1)
    ans.append(q.popleft())

result = "<" + ", ".join(str(i) for i in ans) + ">"
print(result)
