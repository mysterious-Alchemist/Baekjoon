from collections import deque
a = int(input())
lst = [i for i in range(1, a+1)]
dq = deque(lst)
while(len(dq)!=1):
    dq.popleft()
    if(len(dq)>1):
      dq.append(dq[0])
      dq.popleft()    
    
    
print(dq[0])