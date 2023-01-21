import sys
input = sys.stdin.readline
n = int(input())
for i in range(n):
    a,b = map(str, input().split())
    ky = a[-1]
    if ky == "1" or ky == "5" or ky == "6":
        print(ky)
        continue
    elif ky == "4" or ky == "9":
        if int(b[-1]) % 2 == 0:
            atmp = int(ky)
            print(str(atmp**2)[-1])
            continue
        else:
            print(ky)
            continue 
    elif ky == "3" or ky == "7":
        b = int(b) % 4
        atmp = int(ky)
        print(str(atmp**b)[-1])
        continue
    elif ky == "2" or ky == "8":   
        b = int(b) % 4
        if b == 0:
            b = 4
        atmp = int(ky)
        print(str(atmp**b)[-1])
        continue
    elif ky == "0":
        print("10")
        continue
    