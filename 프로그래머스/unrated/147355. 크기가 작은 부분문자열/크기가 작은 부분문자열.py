lst = []
def solution(t, p):
    t = list(map(str, str(t)))
    while(len(t)>=len(p)):
        c = ""
        for i in range(len(p)):
            c = c + t[i]
            #print(f"c = {c}")
            if len(c) == len(p):
                lst.append(c)
        del t[0]
        #print(f"t = {t}")
    ans = 0
    for i in lst:
        if(p>=i):
            ans = ans + 1
    return ans