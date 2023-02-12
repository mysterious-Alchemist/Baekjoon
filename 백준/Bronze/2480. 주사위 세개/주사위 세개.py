a, b, c = map(int, input().split())

t = [a, b, c]
t.sort(reverse=True)
l = t[0]

if a == b == c:
  p = 10000+(a*1000)
elif (a == b) or (a == c) or (b == c):
  if (a == b) or (a == c):
    p = 1000+(a*100)
  else:
    p = 1000+(b*100)
else:
  p = l*100

print(p)