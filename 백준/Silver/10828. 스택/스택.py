import sys
input = sys.stdin.readline

lst = []

def push(lst,x):
    lst.append(x)
    #return lst
def pop(lst):
    if len(lst) == 0:
        print(-1)
    else:
        print(lst[-1])
        del lst[-1]
        #return lst
def size(lst):
    print(len(lst))
def empty(lst):
    if len(lst) == 0:
        print(1)
    else:
        print(0)
def top(lst):
    if len(lst) == 0:
        print(-1)
    else:
        print(lst[-1])

n = int(input())
act = []
for i in range(n):
    a = input().rstrip()
    try:
        a,b = a.split(" ")
        act.append([a,int(b)])
    except:
        act.append(a)

for i in range(len(act)):
    if act[i][0] == "push":
        push(lst,act[i][1])
    else:
        if act[i] == "top":
            top(lst)
        elif act[i] == "size":
            size(lst)
        elif act[i] == "empty":
            empty(lst)
        elif act[i] == "pop":
            pop(lst)
    

    