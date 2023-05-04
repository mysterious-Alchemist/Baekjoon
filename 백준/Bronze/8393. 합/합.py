lst = []
a = int(input())
sum = 0

for i in range(a+1):
    lst.append(i)

for i in lst:
    sum = sum+lst[i]
print(sum)