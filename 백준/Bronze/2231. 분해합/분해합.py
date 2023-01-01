n = int(input())
ans = 0
for i in range(1,n):
    s = sum(map(int, str(i)))
    all = s + i
    if (all == n):
        ans = i
        break
        
print(ans)