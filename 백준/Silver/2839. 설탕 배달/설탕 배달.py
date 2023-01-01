def solu(n):
    if(10>n):
        if((n % 5) == 0):
            print(n // 5)
        elif((n % 3) == 0):
            print(n // 3)
        elif(n == 8):
            print(2)
        else:
            print(-1)
    elif((n % 5) == 0):
        print(n // 5)
    elif ((n-3)%5 == 0 or (n-6)%5 == 0):
        print((n // 5)+1)
    elif((n-9) % 5 == 0 or (n-12) % 5 == 0):
        print((n//5) + 2)
    elif((n % 3) == 0):
        print(n // 3)
    else:
        print(-1)
n = int(input())
solu(n)