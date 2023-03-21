total = int(input())
number = int(input())
sum = 0
for i in range(number)  :
  p, n = map(int, input().split())
  p1 = p*n
  sum = p1 + sum

if(total == sum):
  print("Yes")
else:
  print("No")  