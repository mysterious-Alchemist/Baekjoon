lst_i = []
lst_m = []
for i in range(9):
    globals()['lst'+str(i)] = list(map(int, input().split()))
    a = max(globals()['lst'+str(i)])
    lst_m.append(a)
    lst_i.append( globals()['lst'+str(i)].index(a))

b = max(lst_m)
c = lst_m.index(b)
d = lst_i[c]
print(b)
print(c+1, d+1)