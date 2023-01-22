while(True):
  try:
    a = list (map (int, input()))
    b = a[::-1]
    if (a[0] == 0):
      pass
    elif (a == b):
      print("yes")
    else:
      print("no")
  except EOFError:
    break