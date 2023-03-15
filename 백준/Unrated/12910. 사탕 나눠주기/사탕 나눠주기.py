from collections import Counter
n = int(input())
lst = list(map(int, input().split()))
lst.sort()
ans = []
dic = {}
rst = 0
tmp = 1

for i in range(len(lst)):
    dic[lst[i]] = lst.count(lst[i])

for i in range(1,len(dic)+1):
    if i in dic:
      ans.append(dic[i])
    else:
       break

for i in range(len(ans)):
   tmp = tmp * ans[i]
   rst = rst + tmp
  #  print(ans)
   
print(rst)
