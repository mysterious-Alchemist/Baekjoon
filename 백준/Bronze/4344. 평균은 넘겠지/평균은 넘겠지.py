a = int(input())
all = []
for i in range(a):
    lst = list(map(int, input().split()))
    all.append(lst)

for i in all:
    if(i[0]==1):
        print("0.000%")
    else:
        c = 0
        de = i[0]
        del i[0]
        avg = sum(i) / de
        for k in i:
            if(k>avg):
                c = c + 1
        p = (c/de)*100
        print("{:.3f}%".format(p))