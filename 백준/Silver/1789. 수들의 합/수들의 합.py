s=int(input())
a = 0
if 3>s:
    print(1)
else:
    for i in range(1,s):
        a = i + a
        # print(a)
        if a==s:
            print(i)
            break
        if a>s:
            print(i-1)
            break
