n, k = map(int, input().split())
man = [0]*6
woman = [0]*6
room = 0
for i in range(n):
    s, y = map(int, input().split())
    if s == 0:
        man[y-1] += 1
    else:
        woman[y-1] += 1
# print(man)
# print(woman)
# print(room)
for j in man:
    # print("j", j, "j//k", j//k, "j%k", j%k)
    room += j//k
    if j%k != 0:
        room  += 1 
    # print("room", room) 
for q in woman:
    # print( "q", q, "q//k", q//k, "q%k", q%k)
    room += q//k
    if q%k != 0:
        room  += 1
    # print("room", room)
print(room)