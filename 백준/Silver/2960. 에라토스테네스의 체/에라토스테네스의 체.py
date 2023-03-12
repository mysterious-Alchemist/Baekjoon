c = 0
n, k = map(int, input().split())
lst = [ _ for _ in range(2,n+1)]
while lst:
    num = lst[0]
    del lst[0]
    c = c + 1
    # print(f"num {num}")
    # print(f"c {c}")
    if c == k:
            i = num
            break
    for i in lst:
        # print(f"lst {lst}")
        # print(f"num = {num}")
        # print(f"i = {i}")
        if i%num == 0:
            lst.remove(i)
            c = c + 1
            # print(f"num {num}")
            # print(f"lst {lst}")
            # print(f"c {c}")
            # print(f"i {i}")
            # print()
        if c == k:
            break
    if c == k:
            break

print(i)