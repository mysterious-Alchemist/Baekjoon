dic1 ={
  "c=":"č",
  "c-":"ć",
  "dz=":"dž",
  "d-":"đ",
  "lj":"lj",
  "nj":"nj",
  "s=":"š",
  "z=":"ž"
}

s = input()
c = 0
for i in dic1:
  s=s.replace(i, "x")

print(len(s))