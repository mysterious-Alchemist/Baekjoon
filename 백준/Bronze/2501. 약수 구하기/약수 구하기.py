def get_divisor(n):
    data = []
    for i in range(1, int(n**(0.5))+1):
        if n % i == 0:
            data.append(i)
            if i != n // i:
                data.append(n//i)
    return data
a,b = map(int, input().split())
g=sorted(get_divisor(a))
try:
    print(g[b-1])
except:
    print(0)