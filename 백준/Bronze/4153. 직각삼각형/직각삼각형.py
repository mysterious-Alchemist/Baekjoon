lst = list(map(int, input().split()))
lst.sort()
while(lst[0]!=0):
  if lst[0]**2 + lst[1]**2 == lst[2]**2:
    print("right")
    lst = list(map(int, input().split()))
    lst.sort()
  elif lst[0] == 0 and lst[1] == 0 and lst[2] == 0:
    break
  else:
    print("wrong")
    lst = list(map(int, input().split()))
    lst.sort()