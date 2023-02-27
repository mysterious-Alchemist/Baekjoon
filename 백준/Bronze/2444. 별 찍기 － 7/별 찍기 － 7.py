#백준 2444 별 찍기 - 7
n = int(input())
for i in range(1,(2*n//2)):
    print(" "*(n-i), end = "")
    print("*"*(2*i-1),end = "")
    print()
for i in range((2*n//2),0,-1):
    print(" "*(n-i), end = "")
    print("*"*(2*i-1),end = "")
    print()

