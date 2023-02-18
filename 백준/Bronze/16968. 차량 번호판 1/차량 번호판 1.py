#백준 16968 
k = input()
if k[0] == "c":
     ans = 26
elif k[0] == "d":
     ans = 10
for i in range(len(k)-1):
        if k[i] == k[i+1]:
            if k[i] == "c":
                ans  = ans * 25
            elif k[i] == "d":
                ans = ans * 9
        else:
            if k[i+1] == "c":
                ans = ans * 26
            elif k[i+1] == "d":
                 ans = ans * 10

print(ans)
