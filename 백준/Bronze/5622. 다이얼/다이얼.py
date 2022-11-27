lst = list(input())
l1 = ["A", "B", "C"]
l2 = ["D", "E", "F"]
l3 = ["G", "H", "I"]
l4 = ["J", "K", "L"]
l5 = ["M", "N", "O"]
l6 = ["P", "Q", "R", "S"]
l7 = ["T", "U", "V"]
l8 = ["W", "X", "Y", "Z"]
la = [l1, l2, l3, l4, l5, l6, l7, l8]
c = 0
lc = []
for i in lst:
    for j, k in enumerate(la):
        if(i in la[j]):
            c = j + 3
            lc.append(c)
print(sum(lc))

