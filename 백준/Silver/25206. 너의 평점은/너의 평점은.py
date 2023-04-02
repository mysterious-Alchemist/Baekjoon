#백준 25206 너의 평점은
dic = {
    "A+":4.5,
"A0":4.0,
"B+":3.5,
"B0":3.0,
"C+":2.5,
"C0":2.0,
"D+":1.5,
"D0":1.0,
"F":0.0,
"P":0.0
}
lst = []
lst2 = []
for i in range(20):
    s = input().split()
    if s[2] == "P":
        pass
    else:
        lst.append(float(s[1])*dic[s[2]])
        lst2.append(float(s[1]))
print(f"{sum(lst)/sum(lst2):.6f}")
    