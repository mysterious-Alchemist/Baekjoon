while(True):
    h, m = map(int, input().split())
    if 0<=h<=23:
      if 0<=m<=59:
        break
    
if (h==0):
    if (m>45):
        m=m-45
    elif (m==45):
        m=0
    else:
        h=23
        m=m+15
else:
    if (m>45):
        m=m-45
    elif (m==45):
        m=0
    else:
        h=h-1
        m=m+15
print(h, m)