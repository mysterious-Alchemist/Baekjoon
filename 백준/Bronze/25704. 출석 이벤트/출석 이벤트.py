N=int(input())
P=int(input())

if N>=5 and N<10:
    if (P-500)>0:
        print(P-500)
    else:
        print(0)
elif N>=10 and N<15:
    S = [(P-500),(P*0.9)]
    if 0>=min(S):
        print(0)
    else:
        print(int(min(S)))
elif N>=15 and N<20:
    S = [(P-500),(P*0.9),(P-2000)]
    if 0>=min(S):
        print(0)
    else:
        print(int(min(S)))
elif N>=20 and N<31:
    S = [(P-500),(P*0.9),(P-2000),(P*0.75)]
    if 0>=min(S):
        print(0)
    else:
        print(int(min(S)))
else:
    print(P)