while(True):
  a = int(input())
  if 4001>a>0:
    break

if (a%400==0):
  if (a%4==0):
    print("1")
  else:
     print("0")        
else:
  if (a%100!=0):
    if (a%4==0):
      print("1")
    else:
      print("0")
  else:
    print("0")    