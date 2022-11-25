lst = [i for i in range(1, 31)]

for i in range(28):
    a = int(input())
    if(a in lst):
        lst.remove(a)

if(lst[0]>lst[1]):
    print(lst[1])
    print(lst[0])
else:
    print(lst[0])
    print(lst[1])